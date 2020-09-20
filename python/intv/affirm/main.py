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
                    print(bank)
                    banks[row[0]] = bank
                count += 1
        return banks


class Facility:
    def __init__(self, id, bank_id, ir, capacity):
        self.id = id
        self.bank_id = bank_id
        self.ir = ir
        self.cap = capacity

    def __str__(self):
        return f"Facility: id={self.id}, bank={self.bank_id}, ir={self.ir}, cap={self.cap}"

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
                    print(fac)
                    facilities[row[2]] = fac
                count += 1
        return facilities


class Covenant:
    def __init__(self, fac_id, max_default_likelihood):
        # Since a facility can only associate with one bank, we do not need bank_id here
        self.fac_id = fac_id
        self.max_default_likelihood = max_default_likelihood
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

                    print(cov)
                count += 1
        return covenants


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


if __name__ == '__main__':
    main()