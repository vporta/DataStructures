"""
LookupCSV.py
LookupCSV class
provides a data-driven client for reading in a
 *  key-value pairs from a file; then, printing the values corresponding to the
 *  keys found on standard input. Both keys and values are strings.
 *  The fields to serve as the key and value are taken as command-line arguments.
"""
from SymbolTables.SymbolTable import SymbolTable


class LookupCSV:

    @staticmethod
    def run(f_in, key_field, val_field):
        with open(f_in) as f:
            st = SymbolTable()
            line = f.readline()
            tokens = line.split(',')
            key = tokens[key_field]
            val = tokens[val_field]
            st[key] = val
        if key in st:
            print(st[key])
        else:
            print('not found')


def main():
    file_name = "../Resources/ip.csv"
    key_name, val_name = int(input('Enter key')), int(input('Enter value'))
    LookupCSV.run(file_name, key_name, val_name)


if __name__ == '__main__':
    main()