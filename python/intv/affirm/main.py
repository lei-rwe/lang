import argparse
import os
import sys
import csv


def is_float(s):
    try:
        f = float(s)
        return True, f
    except ValueError:
        return False, None


class Bank:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Bank: id={self.id}, name={self.name}"

    @staticmethod
    def load_banks(banks_file):
        # Read bank information file and create a list of Bank objects
        banks = dict()

        # assume the first row is header
        # Assume the format is: id, name
        with open(banks_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            count = 0
            for row in csvreader:
                if count == 0:
                    pass
                else:
                    bank = Bank(row[0], row[1])
                    banks[row[0]] = bank
                count += 1
        return banks


class Facility:
    def __init__(self, id, bank_id, ir, capacity):
        self.id = id
        self.bank_id = bank_id
        self.ir = float(ir)
        self.max_capacity = float(capacity)
        self.covenant = None

        # Below are status variables
        self.capacity = self.max_capacity
        self.assigned_loans = list()
        self.expected_yields = 0

    def __str__(self):
        return f"Facility: id={self.id}, bank={self.bank_id}, ir={self.ir}, cap={self.max_capacity}, expected_yields={self.expected_yields}." + \
               f"\n\tcovenant={self.covenant}"

    def set_covenant(self, covenant):
        self.covenant = covenant

    def is_loan_legal(self, loan):
        if loan.amount > self.capacity:
            print(f"Facility {self} cannot pick up loan {loan} due to capacity limit")
            return False

        if self.covenant:
            if loan.state and loan.state in self.covenant.banned_states:
                print(f"Facility {self} cannot pick up loan {loan} due to state restriction")
                return False

            if loan.likelihood > self.covenant.max_default_likelihood:
                print(f"Facility {self} cannot pick up loan {loan} due to covenant max default limit")
                return False

        return True

    def assign_loan(self, loan):
        # assign a loan to this facility, which will reduce the capacity
        self.assigned_loans.append(loan)
        self.capacity -= loan.amount
        if self.capacity < 0:
            # should not happen if algorithm is correct, but still double check
            raise ValueError(f"Loan {loan} cannot assign to facility {self}")
        self.calc_yields(loan)
        print(f"Assigned loan {loan} to facility {self}")

    def calc_yields(self, loan):
        # expected_yield = (1 - default_likelihood) * loan_interest_rate * amount
        #                  - default_likelihood * amount\
        #                  - facility_interest_rate * amount
        e = (1 - loan.likelihood) * loan.ir * loan.amount - loan.likelihood * loan.amount - self.ir * loan.amount
        self.expected_yields += e

    @staticmethod
    def load_facilities(facilities_file):
        # Read bank information file and create a list of Bank objects
        facilities = list()

        # assume the first row is header
        # Assume the format is: capacity,interest_rate,id,bank_id
        with open(facilities_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            count = 0
            for row in csvreader:
                if count == 0:
                    pass
                else:
                    fac = Facility(row[2], row[3], row[1], row[0])
                    facilities.append(fac)
                count += 1
        return facilities

    @staticmethod
    def sort_facilities(facilities):
        # This will sort facilities w.r.t the interest rate. So that we can stop at the first legal
        # facility which will hvae the smallest interest rate
        facilities.sort(key=lambda fac: fac.ir)


class Covenant:
    def __init__(self, fac_id, max_default_likelihood):
        # Since a facility can only associate with one bank, we do not need bank_id here
        self.fac_id = fac_id

        a, b = is_float(max_default_likelihood)
        self.max_default_likelihood = b if a else sys.float_info.max

        self.banned_states = set()      # Will aggregate states into a set

    def __str__(self):
        return f"Covenant: fac_id={self.fac_id}, max_default_likelihood={self.max_default_likelihood}, banned_states={self.banned_states}"

    def add_banned_state(self, state):
        if type(state) is set:
            self.banned_states.update(state)
        else:
            self.banned_states.add(state)

    @staticmethod
    def load_covenants(covenants_file):
        # Read covenants information file and create a list of Covenant objects
        # Note that based on the document, facility id may be missing. In this case the covenant will be considered for
        # all the facilities associated with the bank

        bank_covenants = dict()
        covenants = dict()

        # assume the first row is header
        # Assume the format is: facility_id,max_default_likelihood,bank_id,banned_state
        with open(covenants_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            count = 0
            for row in csvreader:
                if count == 0:
                    count += 1
                    continue
                else:
                    count += 1
                    fac_id = row[0]
                    if len(fac_id) == 0:    # covenant is for the bank
                        bank_id = row[2]
                        if len(bank_id) == 0:
                            # both facility id and bank id are empty. Do nothing
                            count += 1
                            continue

                        if bank_id in bank_covenants:
                            cov = bank_covenants[bank_id]
                            cov.add_banned_state(row[3])
                            dft_likeli = row[1]
                            if len(dft_likeli) > 0:
                                dft_likeli = float(dft_likeli)
                                if cov.max_default_likelihood > dft_likeli:
                                    cov.max_default_likelihood = dft_likeli
                        else:
                            cov = Covenant(f"bank_id: {bank_id}", row[1])
                            cov.add_banned_state(row[3])
                            bank_covenants[bank_id] = cov
                        # endif
                    else:
                        if fac_id in covenants:
                            cov = covenants[fac_id]
                            cov.add_banned_state(row[3])
                            dft_likeli = row[1]
                            if len(dft_likeli) > 0:
                                dft_likeli = float(dft_likeli)
                                if cov.max_default_likelihood > dft_likeli:
                                    cov.max_default_likelihood = dft_likeli
                        else:
                            cov = Covenant(fac_id, row[1])
                            cov.add_banned_state(row[3])
                            covenants[fac_id] = cov
                        # endif
                    # endif
                # endif
            # end for
        # end with

        return covenants, bank_covenants

    @staticmethod
    def assign_covenants_to_facilities(facilities, covenants, bank_covenants):
        for fac in facilities:
            if fac.id in covenants:
                cov = covenants[fac.id]
                fac.set_covenant(cov)

            # Add the restrictions for the whole bank
            if bank_covenants and fac.bank_id in bank_covenants:
                bank_cov = bank_covenants[fac.bank_id]
                if fac.covenant:
                    cov = fac.covenant
                    cov.add_banned_state(bank_cov.banned_states)

                    # If bank has small default likelihood, use it
                    dft_likeli = bank_cov.max_default_likelihood
                    if cov.max_default_likelihood > dft_likeli:
                        cov.max_default_likelihood = dft_likeli
                    print(f'Facility {fac} is updated with bank covenant {bank_cov}')
                else:
                    fac.set_covenant(bank_cov)
                    print(f'Facility {fac} is set to bank covenant {bank_cov}')


class Loan:
    def __init__(self, id, amount, ir, likelihood, state):
        self.id = id
        self.ir = float(ir)
        self.amount = float(amount)
        self.state = state
        self.likelihood = float(likelihood)

    def __str__(self):
        return f"Loan: id={self.id}, amount={self.amount}, ir={self.ir}, likelihood={self.likelihood}, state={self.state}"

    @staticmethod
    def process_loans(loans_file, facilities=None, loan_processor_func=None):
        # assume the first row is header
        # Assume the format is: interest_rate,amount,id,default_likelihood,state
        # Return loan_id -> facility_id list for each loan
        loan_assignments = list()
        with open(loans_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            count = 0
            for row in csvreader:
                if count == 0:
                    pass
                else:
                    loan = Loan(row[2], row[1], row[0], row[3], row[4])
                    if loan_processor_func:
                        assignment = loan_processor_func(loan, facilities)
                        loan_assignments.append(assignment)
                    else:
                        print(loan)
                count += 1

        return loan_assignments


def assign_loan_to_facility(loan, faciliies):
    # Since facilities are sorted w.r.t the interest rate, we can stop at the first match
    for fac in faciliies:
        if fac.is_loan_legal(loan):
            fac.assign_loan(loan)
            return loan.id, fac.id
    else:
        print(f"failed to assign loan {loan} to any facility")
        return loan.id, ''


def create_result_files(loan_assignments, facilities, assignment_file, yield_file):
    with open(assignment_file, 'w', newline='\n') as fp:
        wr = csv.writer(fp, quoting=csv.QUOTE_NONE)

        wr.writerow(["loan_id", "facility_id"])

        for assignment in loan_assignments:
            wr.writerow(assignment)

    with open(yield_file, 'w', newline='\n') as fp:
        wr = csv.writer(fp, quoting=csv.QUOTE_NONE)

        wr.writerow(["facility_id", "expected_yield"])

        for fac in facilities:
            wr.writerow([fac.id, round(fac.expected_yields)])


def main():
    ap = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Assign loans to facilities\n" +
                    "\nFor example:" +
                    "\n    python {} -w small -b banks.csv -f facilities.csv -c covenants.csv -l loans.csv -a a.csv -y y.csv".format(sys.argv[0])
    )

    ap.add_argument("-b", "--banks", required=True, type=str, help="Bank file")
    ap.add_argument("-f", "--facilities", required=True, type=str, help="Facilities file")
    ap.add_argument("-c", "--covenants", required=True, type=str, help="Covenants file")
    ap.add_argument("-l", "--loans", required=True, type=str, help="Loans file")

    ap.add_argument("-a", "--assignments", required=True, type=str, help="Assignments file")
    ap.add_argument("-y", "--yields", required=True, type=str, help="yields file")

    ap.add_argument("-w", "--setwd", type=str, help="Directory which holds all the generated data files. Default to current directory")
    ap.add_argument("-z", "--debug", action='store_true', help="If specified, program will involve pdb.set_trace() at the beginning")

    args = ap.parse_args()

    if args.debug:
        import pdb; pdb.set_trace()

    if args.setwd:
        working_dir = args.setwd
    else:
        working_dir = "."

    banks = Bank.load_banks(os.path.join(working_dir, args.banks))

    facilities = Facility.load_facilities(os.path.join(working_dir, args.facilities))
    Facility.sort_facilities(facilities)

    covenants, bank_cov = Covenant.load_covenants(os.path.join(working_dir, args.covenants))

    Covenant.assign_covenants_to_facilities(facilities, covenants, bank_cov)

    print("Facilities with covenants:")
    for fac in facilities:
        print(f"{fac}")

    loan_assignments = Loan.process_loans(os.path.join(working_dir, args.loans),
                                          facilities=facilities,
                                          loan_processor_func=assign_loan_to_facility)

    create_result_files(loan_assignments, facilities, args.assignments, args.yields)


if __name__ == '__main__':
    main()