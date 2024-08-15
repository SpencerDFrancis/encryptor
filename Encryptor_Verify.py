# -*- coding: utf-8 -*-
"""
                            Encryptor - Verify
Author: S D Francis

Uses words.txt to verify that a cypher has been successfully decrypted.
"""

import string
import Encryptor_Messages as ms

def findFile(language):
    if language == 'english':
        filepath = 'languages\\english.txt'
    elif language == 'arabic':
        filepath = 'languages\\arabic.txt'
    elif language == 'czech':
        filepath = 'languages\\czech.txt'
    elif language == 'danish':
        filepath = 'languages\\danish.txt'
    elif language == 'dutch':
        filepath = 'languages\\dutch.txt'
    elif language == 'esperanto':
        filepath = 'languages\\esperanto.txt'
    elif language == 'french':
        filepath = 'languages\\french.txt'
    elif language == 'georgian':
        filepath = 'languages\\georgian.txt'
    elif language == 'german':
        filepath = 'languages\\german.txt'
    elif language == 'greek':
        filepath = 'languages\\greek.txt'
    elif language == 'hebrew':
        filepath = 'languages\\hebrew.txt'
    elif language == 'italian':
        filepath = 'languages\\italian.txt'
    elif language == 'latin':
        filepath = 'languages\\latin.txt'
    elif language == 'norwegian':
        filepath = 'languages\\norwegian.txt'
    elif language == 'polish':
        filepath = 'languages\\polish.txt'
    elif language == 'portuguese' or language == 'brazilian':
        filepath = 'languages\\portuguese.txt'
    elif language == 'russian':
        filepath = 'languages\\russian.txt'
    elif language == 'serbian':
        filepath = 'languages\\serbian.txt'
    elif language == 'spanish':
        filepath = 'languages\\spanish.txt'
    elif language == 'swedish':
        filepath = 'languages\\swedish.txt'
    elif language == 'turkish':
        filepath = 'languages\\turkish.txt'
    elif language == 'ukranian':
        filepath = 'languages\\ukranian.txt'
    else:
        raise ValueError(ms.language)
    
    with open(filepath, "r") as file:
        wordlist = [line.strip().lower() for line in file.readlines()]
    
    return wordlist

# What portion of words in sentence are known english words
def compare(message, language='english'):
    # Choose a wordlist
    wordlist = findFile(language)
    
    # Split message into words
    sentence = message.split()
    
    # Tally how many words are known
    known = 0
    total = len(sentence)
    
    for word in sentence:
        # Remove punctuation from the word
        naked = word.translate(str.maketrans('', '', string.punctuation))
        if naked.lower() in wordlist:
            known += 1
        elif not [*naked]:
            continue
        elif [*naked][0] in list('1234567890'):
            known += 1
    
    if total > 0:
        ratio = known / total
    else:
        ratio = 0
    
    return ratio

def report(key, ratio):
    print(f'Key: {key}.................{ratio:.2f}%')

def test():
    test_message = 'We hold these truths to be self evident: skibidi toilet'
    key = 3
    p = 100 * compare(test_message, 'english')
    report(key, p)

def main():
    print('What language would you like to test for?')
    language = input().strip().lower()
    wordlist = findFile(language)
    print(f'Loaded wordlist for {language}. Contains {len(wordlist)} words.')
    print()
    message = input('Enter Text: ')
    print()
    ratio = 100 * compare(message,language)
    print(f'Given text contains {ratio}% known words in {language}')
    

if __name__ == '__main__':
    #test()
    main()
