import argparse
from cipher import Cipher

if __name__ == "__main__":
    parser = argparse.ArgumentParser()                                                      # Creating parser which will hold all the information necessary
                                                                                            # to parse command line into Python data types
    parser.add_argument("file", help = "File to be encrypted or decrypted.")                # File name to be taken from CLI
    parser.add_argument("key", help = "Number by which letter to be shifted.")              # Key value '' '' ''''' '''' '''
    parser.add_argument("operation", help = "Operation: e - encryption or d - decryption.") # Ciphering option '' '' ''''' '''' '''

    args = parser.parse_args()                 # Allows converting arguement strings to objects and assign them as attributes of the namespace

    ciph = Cipher(args.file)                   # Creating Cipher object  - ciph to which file name entered from CLI is passed as argument
    ciph.caesar(int(args.key), args.operation) # Method - caesar is called on ciph objects to which key value and operation parameter from CLI is passed
