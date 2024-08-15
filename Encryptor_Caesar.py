# -*- coding: utf-8 -*-
"""
                            Encryptor - Caesar
Author: S D Francis

Decrypt and encrypt caesar cyphers with Encryptor.
"""
import Encryptor_Alphabets
import Encryptor_Verify as ver
import re

# Caesar Cipher
def caesar(message, intkey, alphabet):
    original = [*message]
    output = []
    n = len(alphabet)  # Length of the alphabet
    
    for char in original:
        lower_char = char.lower()
        
        if lower_char in alphabet:
            index = alphabet.index(lower_char)
            new_index = (index + intkey) % n
            out = alphabet[new_index]
        else:
            out = char
        
        output.append(out)
        
    return ''.join(output)  # Join the output list into a string

# Decrypt message  
def read(message, key, alphabet):
    decrypted = caesar(message, -key, alphabet)  # Use negative key for decryption
    return decrypted

# Encrypt message    
def write(message, key, alphabet): 
    encrypted = caesar(message, key, alphabet)
    return encrypted

# Decrypt message with unknown key
def unknown(message, alphabet, language):
    keys = range(1, len(alphabet))  # List of all possible keys
    
    # Load a dictionary to hold messages
    allTrials = {'Original': [message, 100 * ver.compare(message, language)]}
    
    # Populate the dictionary with possible translations
    for k in keys:
        trial = read(message, k, alphabet)  # Decode with a certain key
        p = 100 * ver.compare(trial, language)  # Percentage accurate
        allTrials[str(k)] = [trial, p]
    
    # Create lists of decryptions
    excellent = []  # Over 95% known words
    good = []  # Over 80% known words
    sortedDecryptions = []  # All translations sorted by accuracy

    # First populate the sorted list
    for k in allTrials.keys():
        if k != 'Original':
            item = allTrials[k]  # Fetch dictionary element
            p = item[1]
            inserted = False
            for i, sk in enumerate(sortedDecryptions):  # For each item already in the list
                comp = allTrials[sk]  # Fetch percentage
                pcomp = comp[1]
                if p >= pcomp:  # If this decryption is better
                    sortedDecryptions.insert(i, k)  # Insert to the left
                    inserted = True
                    break  # Exit the loop
            if not inserted:
                sortedDecryptions.append(k)  # Just add to the end

    # Populate the other lists
    for k in sortedDecryptions:
        item = allTrials[k]  # Fetch dictionary element
        p = item[1]
        if p >= 95:
            excellent.append(k)
        if p >= 80:
            good.append(k)
    
    # Report back to console
    if len(excellent) > 0:
        print(f'We have found {len(excellent)} with matches over 95% confidence.\n')
        for k in excellent:  # List them
            p = allTrials[k][1]
            ver.report(k, p)
    elif len(good) > 0:
        print(f'We have found {len(good)} with matches over 80% confidence.\n')
        for k in good:  # List them
            p = allTrials[k][1]
            ver.report(k, p)
    else:
        print(f'Highest match has {allTrials[sortedDecryptions[0]][1]}% confidence.')
        for k in sortedDecryptions:  # List them
            p = allTrials[k][1]
            ver.report(k, p)
    
    investigating = True
    
    while investigating:
        print('If you would like to see all matches type \'list\' or to read a decryption simply type \'read [key]\'.')
        action = input().lower()
    
        if action == 'list':
            for k in sortedDecryptions:  # List them
                p = allTrials[k][1]
                ver.report(k, p) 
    
        elif re.search('read ', action):
            s = action.replace('read', '')
            subject = s.strip()
            
            if subject in sortedDecryptions:
                print(f'Key: {subject} is in position {sortedDecryptions.index(subject)} and has {allTrials[subject][1]}% known words.')
                print('It reads:')
                print(allTrials[subject][0])
            else:
                print(f'Sorry, key \"{subject}\" is not on the list.')
        
        elif action == 'help':
            print('If you would like to see all matches type \'list\' or to read a decryption simply type read [key].')
        
        elif action == 'c':
            investigating = False
            print('Exiting...')
            
        else:
            print(error)

error = """
I'm sorry. I don't think I understand. Please enter a valid option
or type help to see commands.
"""

help_message = """
Your options are:
    read - read an encrypted message with either a known or unknown key
    write - encrypt a message
    c - exit
"""

# Main Function
def main():
    running = True
    alphabet = None
    language = None
    
    # Choose an alphabet
    alphabet, language = Encryptor_Alphabets.chooseAlphabet()
        
    # if no alphabet selected, break from the loop
    if alphabet is None:
        running = False
        return
    
    while running:
        message = None
        key = None

        # Writing or reading
        print()
        print('Would you like to write or read?')
        choice = input().lower()
        
        # Reading
        if choice == 'read':
            print('Is the key known or unknown?')
            choice = input().lower()
            
            # Known
            if choice == 'known':
                key = int(input('Please enter key: '))
                message = input('Please enter message: ')
                decrypted = read(message, key, alphabet) 
                print()
                print(f'Decrypted message: {decrypted}')
                
            # Unknown
            elif choice == 'unknown':
                message = input('Please enter message: ')
                print()
                print('...decrypting message...')
                print()
                unknown(message, alphabet, language)
        
        # Writing
        elif choice == 'write':
            key = int(input('Please enter key: '))
            message = input('Please enter message: ')
            encrypted = write(message, key, alphabet)
            print()
            print(f'Encrypted message: {encrypted}')
            
        elif choice == 'help':
            print(help_message)
    
        elif choice == 'c':
            running = False
            
        else:
            print(error)
        
if __name__ == '__main__':
    main()
