# -*- coding: utf-8 -*-
"""
                                    Encryptor
Author: S D Francis


This is the wrapper file for Encryptor.
"""

import Encryptor_Messages as ms
import Encryptor_Caesar as caesar
import Encryptor_Columnar as columnar


def main():
    
    # Print intro message 
    print(ms.intro)
    
    Prunning = True
    
    while Prunning == True:
        # Print prompt
        print(ms.prompt)
    
        # Ask for input
        Command = input()
        command = Command.lower()
        
        # C to quit
        if command == 'c':
            print(ms.outro)
            Prunning = False
        
        if command == 'x':
            print(ms.outro)
            Prunning = False
        
        # Help message
        elif command == 'help':
            print(ms.help)
            
        # Send to Caesar Cypher mode
        elif command == 'caesar':
            print('Loading Caesar Cypher')
            print()
            caesar.main()
    
        # Send to Columnar Cypher mode
        elif command == 'columnar':
            print('Loading Columnar Cypher')
            print()
            columnar.main()
   
        # If the prompt is unintelligable
        else:
            print(ms.confusion)
            
    




if __name__ == '__main__':
    main()

