import os

class Cipher:
    """
    Description
    -----------
        Module used for encrypting and decrypting letters in text files using caesar cipher algorithm.
        It is executed using command line interface.
    
    Concepts covered
    -------- -------
        - Looping
        - Tuples and Dictonaries
        - Conversion of a letter to its ascii value using function ord('<letter>') and vice versa using chr(<ascii number value>)
        - Basic Object Oriented Programming
        - File handling

    Notes
    -----
        - Letter(s) are treated as numbers from 0 - 25 for shifting purpose - letter_number to represent particular letter. 
        e.g a or A: letter_number = 0, b or B: letter_number = 1,....z or Z: letter_number = 25
        - To reduce time complexity, dictionaries are predefined instead of using loop for mapping over and over...
    
    ...
    
    Attributes
    ----------
        ascii_lower_pos: dict
            it allows lower values of ascii to be mapped to letter number
        
        ascii_upper_pos: dict
            it allows upper values of ascii to be mapped to letter number

        map_to_ascii: dict
            it allows mapping of letter numbers to both of its lowercase and uppercase ascii values
        
        file: str
            holds the file object which is to be encrypted or decrypted  
    
    ...

    Methods
    -------
        shift_letter_number(letter_number, key, operation):
            returns new letter number after being shifted by some number of positions (key value)
        
        cipher_alphabet(letter, key, operation):
            returns rotated alphabet. This method is written such that shift_letter_number works only on letters not characters
        
        caesar(key, operation):
            performs encryption or decryption of the letters in text files        
    """

    def __init__(self, filename):
        """
        Parameter
        ---------
            filename:
                name of the file which is to be encrypted or decrypted
        """

        self.ascii_lower_pos = {97: 0, 98: 1, 99: 2, 100: 3,  
                            101: 4, 102: 5, 103: 6, 104: 7, 
                            105: 8, 106: 9, 107: 10, 108: 11, 
                            109: 12, 110: 13, 111: 14, 112: 15, 
                            113: 16, 114: 17, 115: 18, 116: 19, 
                            117: 20, 118: 21, 119: 22, 120: 23, 
                            121: 24, 122: 25}
        
        self.ascii_upper_pos = {65: 0, 66: 1, 67: 2, 68: 3, 
                            69: 4, 70: 5, 71: 6, 72: 7,
                            73: 8, 74: 9, 75: 10, 76: 11,
                            77: 12, 78: 13, 79: 14, 80: 15, 
                            81: 16, 82:17, 83: 18, 84: 19, 
                            85: 20, 86: 21, 87: 22, 88: 23, 
                            89: 24, 90: 25}
        
        self.map_to_ascii = {0: (97, 65), 1: (98, 66), 2: (99, 67), 3: (100, 68),
                            4: (101, 69), 5: (102, 70), 6: (103, 71), 7: (104, 72),
                            8: (105, 73), 9: (106, 74), 10: (107, 75), 11: (108, 76),
                            12: (109, 77), 13: (110, 78), 14: (111, 79), 15: (112, 80),
                            16: (113, 81), 17: (114, 82), 18: (115, 83), 19: (116, 84),
                            20: (117, 85), 21: (118, 86), 22: (119, 87), 23: (120, 88),
                            24: (121, 89), 25: (122, 90)}
        
        self.file = filename
    
    def shift_letter_number(self, letter_number, key, operation):
        """Returns new letter number after being shifted by some number of positions (key value).
        
        Parameters
        ----------
            letter_number: int
                it is alphabet in its numerical format
            key: int
                number of letter_numbers by which the letter is to be shifted either left or right
            operation: str
                shift to be performed either on right - encryption: "e" or left - decryption: "d"

        Return
        ------
            new alphabet in numerical form
        """
        if operation == "e":
            return (letter_number + key) % 26                                       # If encryption is to be performed, (letter_number + key) % 26 will be returned.
        if operation == "d":
            return (letter_number - key) % 26                                       # If decryption, (letter_number - key) % 26 will be returned. Either of this will be the new letter_number

    def new_letter(self, letter, key, operation):
        """Returns rotated alphabet. This method is written such that shift_letter_number works only on letters not other characters.

        Parameters
        ----------
            letter: str
                it is the letter which is to be shifted
            key: int
                number of positions by which the letter is to be shifted either left or right
            operation: str
                shift to be performed either on right - encryption: "e" or left - decryption: "d"

        Returns
        -------
            tuple which consists of:
                new_character: str
                    letter after its being rotated
                ascii_range: bool
                    true if ascii value lies in range of lowercase and uppercase ascii values else false
        """
        letter_number = -1                                                          # Initialization of letter number
        flag = -1                                                                   # Initialization of flag
                                                                                    # This will allow accessing either lowercase or uppercase ascii value of a letter      
        
        ascii_value = ord(letter)                                                   # Conversion of letter to its ascii value

        ascii_lowercase_range = ascii_value >= 97 and ascii_value <= 122            # Boolean value stores true if ascii value lies between 97 and 122
        ascii_uppercase_range = ascii_value >= 65 and ascii_value <= 90             # Boolean value stores true if ascii value lies between 65 and 90
        ascii_range = ascii_lowercase_range or ascii_uppercase_range                # Boolean value stores true if ascii value lies within 97 and 122 or 65 and 90
        
        if ascii_uppercase_range:
            letter_number = self.ascii_upper_pos[ascii_value]                       # Numerical representation of alphabet is returned
            flag = 1                                                                # This will allow access of upper case ascii value
        
        if ascii_lowercase_range:
            letter_number = self.ascii_lower_pos[ascii_value]
            flag = 0                                                                # This will allow access of lower case ascii value
            
        new_letter_number = self.shift_letter_number(letter_number, key, operation)   # New alphabet in numerical form
        new_character = chr(self.map_to_ascii[new_letter_number][flag])             # Ascii value of new alphabet is returned from map_to_ascii dictionary.
                                                                                    # chr function allows conversion of this ascii value back to new alphabet    
        
        return new_character, ascii_range                                           # Returns new alphabet and bool ascii value check 


    def caesar(self, key, operation):
        """Performs encryption or decryption of the letters in text files.     
        
        Parameters
        ----------
            key: int
                number of positions by which the letter is to be shifted either left or right
            operation: str
                shift to be performed either on right - encryption: "e" or left - decryption: "d"
        """
        tempFilename, cipherText = {"e": "encrypt.txt", "d": "decrypt.txt"}, ''     # tempFilename - stores names of the temporary files    
                                                                                    # cipherText stores the encrypted or deciphered text
        # To raise error if key entered is greater than 26
        if key > 26:
            raise KeyError("Number of positions to be shifted is out of range. Please enter new key value.")
        
        # To raise error if parameters other than e or d is entered
        if operation not in ('e', 'd'):
            raise ValueError("Invalid encryption or decryption option! Select only 'e' or 'd'.")

        # Check if file is already encrypted and/or key by the entered is correct or not
        checkList, checkFile = [], ".check.txt"
        file_exists = os.path.isfile(".check.txt")
        if not file_exists:
            with open(checkFile, mode='w') as wc:
                wc.write("")
        
        with open(checkFile, mode='r') as c:
            checkList = c.readline().split()
            if checkList != []:
                if checkList[0] == operation:
                    raise ValueError("File already encrypted!")
                if checkList[1] != str(key):
                    raise KeyError("Invalid key! Enter the key which was used for encryption.")

        with open(self.file, mode='r+') as rf:                                      # Opens the file to be encrypted and is read line by line
            for message in rf:
                for character in message:
                    if self.new_letter(character, key, operation)[1]:               # Check performed whether its a letter or other character
                        cipherText += self.new_letter(character, key, operation)[0] # New letter is returned and is concatenated to the cipher text
                    else:
                        cipherText += character                                     # If character is not a letter, it will be concatenated to the cipher text
                    
                with open(tempFilename[operation], mode = 'w') as wf:               # Writes the cipher text to the temporary file
                    wf.write(cipherText)
        
        os.remove(self.file)                                                        # Removes old file
        os.rename(tempFilename[operation], self.file)                               # Temporary file is renamed as the original name of the file

        # If file to be encrypted, the hidden text file .check.txt will store the flag - e and key value - 20
        if operation == "e":
            with open(checkFile, mode='w') as wc:
                wc.write("e" + " " + str(key))
            print("\nFile encrypted successfully!\n")
        
        # If file to be decrypted, the hidden text file .check.txt will be removed
        if operation == "d":
            os.remove(checkFile)
            print("\nFile decrypted successfully!\n")