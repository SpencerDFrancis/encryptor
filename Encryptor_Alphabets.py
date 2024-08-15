# -*- coding: utf-8 -*-
"""
                            Encryptor - Alphabets
Author: S D Francis

List of alphabets for Encryptor.
"""
import Encryptor_Messages as ms

def chooseAlphabet():
    alphabet = None
    language = None
    
    while alphabet is None:
        print('What language would you like to use?')
        choice = input().lower()
        
        if choice == 'english':
            language = 'english'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading English (Letters and numbers)')
                alphabet = iso_mix
            elif y == 'no':
                print('Loading English (Letters Only)')
                alphabet = iso_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'arabic':
            language = 'arabic'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Arabic (Letters and numbers)')
                alphabet = arabic_mix
            elif y == 'no':
                print('Loading Arabic (Letters Only)')
                alphabet = arabic_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'croatian':
            language = 'croatian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Croatian (Letters and numbers)')
                alphabet = croatian_mix
            elif y == 'no':
                print('Loading Croatian (Letters Only)')
                alphabet = croatian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'danish':
            language = 'danish'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Danish (Letters and numbers)')
                alphabet = danish_mix
            elif y == 'no':
                print('Loading Danish (Letters Only)')
                alphabet = danish_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'dutch':
            language = 'dutch'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Dutch (Letters and numbers)')
                alphabet = dutch_mix
            elif y == 'no':
                print('Loading Dutch (Letters Only)')
                alphabet = dutch_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'esperanto':
            language = 'esperanto'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Esperanto (Letters and numbers)')
                alphabet = esperanto_mix
            elif y == 'no':
                print('Loading Esperanto (Letters Only)')
                alphabet = esperanto_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'french':
            language = 'french'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading French (Letters and numbers)')
                alphabet = french_mix
            elif y == 'no':
                print('Loading French (Letters Only)')
                alphabet = french_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'georgian':
            language = 'georgian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Georgian (Letters and numbers)')
                alphabet = georgian_mix
            elif y == 'no':
                print('Loading Georgian (Letters Only)')
                alphabet = georgian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'german':
            language = 'german'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading German (Letters and numbers)')
                alphabet = german_mix
            elif y == 'no':
                print('Loading German (Letters Only)')
                alphabet = german_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'greek':
            language = 'greek'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Greek (Letters and numbers)')
                alphabet = greek_mix
            elif y == 'no':
                print('Loading Greek (Letters Only)')
                alphabet = greek_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'hebrew':
            language = 'hebrew'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Hebrew (Letters and numbers)')
                alphabet = hebrew_mix
            elif y == 'no':
                print('Loading Hebrew (Letters Only)')
                alphabet = hebrew_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'italian':
            language = 'italian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Italian (Letters and numbers)')
                alphabet = italian_mix
            elif y == 'no':
                print('Loading Italian (Letters Only)')
                alphabet = italian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'norwegian':
            language = 'norwegian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Norwegian (Letters and numbers)')
                alphabet = norwegian_mix
            elif y == 'no':
                print('Loading Norwegian (Letters Only)')
                alphabet = norwegian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'polish':
            language = 'polish'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Polish (Letters and numbers)')
                alphabet = polish_mix
            elif y == 'no':
                print('Loading Polish (Letters Only)')
                alphabet = polish_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'portuguese' or choice == 'brazilian':
            language = 'portuguese'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Portuguese (Letters and numbers)')
                alphabet = portuguese_mix
            elif y == 'no':
                print('Loading Portuguese (Letters Only)')
                alphabet = portuguese_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'russian':
            language = 'russian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Russian (Letters and numbers)')
                alphabet = russian_mix
            elif y == 'no':
                print('Loading Russian (Letters Only)')
                alphabet = russian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'serbian':
            language = 'serbian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Serbian (Letters and numbers)')
                alphabet = serbian_mix
            elif y == 'no':
                print('Loading Serbian (Letters Only)')
                alphabet = serbian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'spanish':
            language = 'spanish'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Spanish (Letters and numbers)')
                alphabet = spanish_mix
            elif y == 'no':
                print('Loading Swedish (Letters Only)')
                alphabet = swedish_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'swedish':
            language = 'swedish'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Swedish (Letters and numbers)')
                alphabet = swedish_mix
            elif y == 'no':
                print('Loading Swedish (Letters Only)')
                alphabet = swedish_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'turkish':
            language = 'turkish'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Turkish (Letters and numbers)')
                alphabet = turkish_mix
            elif y == 'no':
                print('Loading Turkish (Letters Only)')
                alphabet = turkish_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'ukrainian':
            language = 'ukrainian'
            print('Would you like to include digits as well? (Yes/No)')
            y = input().lower()
            if y == 'yes':
                print('Loading Ukrainian (Letters and numbers)')
                alphabet = ukrainian_mix
            elif y == 'no':
                print('Loading Ukrainian (Letters Only)')
                alphabet = ukrainian_letters
            elif y == 'c':
                print('Exiting...')
                break
            else:
                print('Invalid choice. Please enter Yes, No, or C to cancel.')

        elif choice == 'c':
            print('Exiting')
            break
        
        else:
            print(ms.language)
            
    return alphabet, language


# English letters only
iso_letters = list('abcdefghijklmnopqrstuvwxyz')
# English letters and numbers
iso_mix = list('abcdefghijklmnopqrstuvwxyz0123456789')

# Arabic letters only
arabic_letters = list('ابتثجحخدذرزسشصضطظعغفقكلمنهوي')
# Arabic letters and numbers
arabic_mix = list('ابتثجحخدذرزسشصضطظعغفقكلمنهوي٠١٢٣٤٥٦٧٨٩')

# Croatian letters only
croatian_letters = list('abcčćdđefghijklmnopqrsštuvwxyzž')
# Croatian letters and numbers
croatian_mix = list('abcčćdđefghijklmnopqrsštuvwxyzž0123456789')

# Danish letters only
danish_letters = list('abcdefghijklmnopqrstuvwxyzæøå')
# Danish letters and numbers
danish_mix = list('abcdefghijklmnopqrstuvwxyzæøå0123456789')

# Dutch letters only
dutch_letters = list('abcdefghijklmnopqrstuvwxyz')
# Dutch letters and numbers
dutch_mix = list('abcdefghijklmnopqrstuvwxyz0123456789')

# Esperanto letters only
esperanto_letters = list('abcĉdefgĝhĥijĵklmnoprsŝtuŭvz')
# Esperanto letters and numbers
esperanto_mix = list('abcĉdefgĝhĥijĵklmnoprsŝtuŭvz0123456789')

# French letters only
french_letters = list('abcdefghijklmnopqrstuvwxyz') #àâæçéèêëîïôœùûüÿ
# French letters and numbers
french_mix = list('abcdefghijklmnopqrstuvwxyz0123456789') #àâæçéèêëîïôœùûüÿ

# Georgian letters only
georgian_letters = list('აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ')
# Georgian letters and numbers
georgian_mix = list('აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ0123456789')

# German letters only
german_letters = list('abcdefghijklmnopqrstuvwxyzäöüß')
# German letters and numerals
german_mix = list('abcdefghijklmnopqrstuvwxyzäöüß0123456789')

# Greek letters only
greek_letters = list('αβγδεζηθικλμνξοπρστυφχψω')
# Greek lettersand numbers
greek_mix = list('αβγδεζηθικλμνξοπρστυφχψω0123456789')

# Hebrew letters only
hebrew_letters = list('אבגדהוזחטיכלמנסעפצקרשת')
# Hebrew letters and numbers
hebrew_mix = list('אבגדהוזחטיכלמנסעפצקרשת0123456789')

# Italian letters only
italian_letters = list('abcdefghijklmnopqrstuvwxyz')
# Italian letters and numbers
italian_mix = list('abcdefghijklmnopqrstuvwxyz0123456789')

# Latin letters only (same as English in this case)
latin_letters = list('abcdefghijklmnopqrstuvwxyz')
# Latin letters and numerals (same as English in this case)
latin_mix = list('abcdefghijklmnopqrstuvwxyz0123456789')

# Norwegian letters only
norwegian_letters = list('abcdefghijklmnopqrstuvwxyzæøå')
# Norwegian lettersand numbers
norwegian_mix = list('abcdefghijklmnopqrstuvwxyzæøå0123456789')

# Polish letters only
polish_letters = list('aąbcćdeęfghijklłmnńopqrsśtuvwxyzźż')
# French lettersand numbers
polish_mix = list('aąbcćdeęfghijklłmnńopqrsśtuvwxyzźż0123456789')

# Portuguese letters only
portuguese_letters = list('abcdefghijklmnopqrstuvwxyz') #áâãàçéêíóôõúü
# Portuguese letters and numbers
portuguese_mix = list('abcdefghijklmnopqrstuvwxyz0123456789') #áâãàçéêíóôõúü

# Russian letters only
russian_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
# Russian letters and numbers
russian_mix = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789')

# Serbian letters only
serbian_letters = list('абвгдђежзијклљмнњопрстћуфхцчџш')
# French lettersand numbers
serbian_mix = list('абвгдђежзијклљмнњопрстћуфхцчџш0123456789')

# Spanish letters only
spanish_letters = list('abcdefghijklmnñopqrstuvwxyz')
# Spanish letters and numerals
spanish_mix = list('abcdefghijklmnñopqrstuvwxyz0123456789')

# Swedish letters only
swedish_letters = list('abcdefghijklmnopqrstuvwxyzåäö')
# Swedish lettersand numbers
swedish_mix = list('abcdefghijklmnopqrstuvwxyzåäö')

# Turkishletters only
turkish_letters = list('abcçdefgğhıijklmnoöprsştuüvyzqwx')
# Turkish lettersand numbers
turkish_mix = list('abcçdefgğhıijklmnoöprsştuüvyzqwx')

# Ukrainian letters only
ukrainian_letters = list('абвгґдеєжзиіїйклмнопрстуфхчшщьюя')
# Ukrainian lettersand numbers
ukrainian_mix = list('абвгґдеєжзиіїйклмнопрстуфхчшщьюя')

def main():
    chooseAlphabet()

if __name__ == '__main__':
    main()
