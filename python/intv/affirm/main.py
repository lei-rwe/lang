import argparse
import os
import sys
import csv


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

    def __str__(self):
        return f"Facility: id={self.id}, bank={self.bank_id}, ir={self.ir}, cap={self.max_capacity}.\n\tcovenant={self.covenant}"

    def set_covenant(self, covenant):
        self.covenant = covenant

    def is_loan_legal(self, loan):
        if loan.amount > self.capacity:
            return False

        if self.covenant:
            if loan.state and loan.state in self.covenant.banned_states:
                return False
            if loan.likelihood > self.covenant.max_default_likelihood:
                return False

        return True

    def assign_loan(self, loan):
        # assign a loan to this facility, which will reduce the capacity
        self.assigned_loans.append(loan)
        self.capacity -= loan.amount
        if self.capacity < 0:
            # should not happen if algorithm is correct, but still double check
            raise ValueError(f"Loan {loan} cannot assign to facility {self}")
        print(f"Assigned loan {loan} to facility {self}")

    @staticmethod
    def load_facilities(facilities_file):
        # Read bank information file and create a list of Bank objects
        facilities = dict()

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
                    facilities[row[2]] = fac
                count += 1
        return facilities


class Covenant:
    def __init__(self, fac_id, max_default_likelihood):
        # Since a facility can only associate with one bank, we do not need bank_id here
        self.fac_id = fac_id
        if max_default_likelihood.isnumeric():
            self.max_default_likelihood = float(max_default_likelihood)
        else:
            self.max_default_likelihood = sys.float_info.max

        self.banned_states = set()      # Will aggregate states into a set

    def __str__(self):
        return f"Covenant: fac_id={self.fac_id}, max_default_likelihood={self.max_default_likelihood}, banned_states={self.banned_states}"

    def add_banned_state(self, state):
        self.banned_states.add(state)

    @staticmethod
    def load_covenants(covenants_file):
        # Read bank information file and create a list of Covenant objects
        covenants = dict()

        # assume the first row is header
        # Assume the format is: facility_id,max_default_likelihood,bank_id,banned_state
        with open(covenants_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            count = 0
            for row in csvreader:
                if count == 0:
                    pass
                else:
                    fac_id = row[0]
                    if fac_id in covenants:
                        cov = covenants[fac_id]
                        cov.add_banned_state(row[3])
                    else:
                        cov = Covenant(fac_id, row[1])
                        covenants[fac_id] = cov
                        cov.add_banned_state(row[3])

                count += 1
        return covenants

    @staticmethod
    def assign_covenants_to_facilities(facilities, covenants):
        for fac_id, cov in covenants.items():
            if fac_id in facilities:
                facilities[fac_id].set_covenant(cov)


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
        with open(loans_file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            count = 0
            for row in csvreader:
                if count == 0:
                    pass
                else:
                    loan = Loan(row[2], row[1], row[0], row[3], row[4])
                    if loan_processor_func:
                        loan_processor_func(loan, facilities)
                    else:
                        print(loan)
                count += 1


def assign_loan_to_facility(loan, faciliies):
    # Iterator the facilities and pickup the legal one with minimum interest
    min_ir = 1.0
    min_ir_fac = None
    for fac_id, fac in faciliies.items():
        if fac.is_loan_legal(loan):
            if fac.ir < min_ir:
                min_ir = fac.ir
                min_ir_fac = fac
    if min_ir_fac:
        min_ir_fac.assign_loan(loan)
    else:
        print(f"failed to assign loan {loan} to any facility")


def main():
    ap = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Assign loans to facilities\n" +
                    "\nFor example:" +
                    "\n    python {} ".format(sys.argv[0])
    )

    ap.add_argument("-b", "--banks", required=True, type=str, help="Bank file")
    ap.add_argument("-f", "--facilities", required=True, type=str, help="Facilities file")
    ap.add_argument("-c", "--covenants", required=True, type=str, help="Covenants file")
    ap.add_argument("-l", "--loans", required=True, type=str, help="Loans file")
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
    print(banks)

    facilities = Facility.load_facilities(os.path.join(working_dir, args.facilities))
    print(facilities)

    covenants = Covenant.load_covenants(os.path.join(working_dir, args.covenants))
    print(covenants)

    Covenant.assign_covenants_to_facilities(facilities, covenants)

    for fac_id, fac in facilities.items():
        print(f"{fac}")

    Loan.process_loans(os.path.join(working_dir, args.loans),
                       facilities=facilities,
                       loan_processor_func=assign_loan_to_facility)


if __name__ == '__main__':
    main()