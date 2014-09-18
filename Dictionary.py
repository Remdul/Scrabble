from __future__ import print_function

import csv

def importFile(listWords):
    with open('words.csv', 'rb') as csvfile:
        wordReader = csv.reader(csvfile)
        for row in wordReader:
            row = "".join(row)
            listWords.append(row)

def has_dup(sortedWords):
    return len(sortedWords) != len(set(sortedWords))

def find_dup(sortedWords, listWords):
    s= set()
    duplicateWords = set()
    wordnum = 0
    for word in sortedWords:
        wordnum += 1
        if word in s - duplicateWords:
            yield word
            duplicateWords.add(word)
            print(listWords[wordnum])

        else:
            s.add(word)


def main():
    listWords = []
    sortedWords = []
    importFile(listWords)
    listWords.sort()

    for i in range(len(listWords)):
        sortedWords.append(''.join(sorted(listWords[i])))

    for i in range(len(sortedWords)):
        print(sortedWords[i])
        print(listWords[i])
    print ("Are there Anagrams:" , has_dup(sortedWords))
    print ("Anagram words: " , list(find_dup(sortedWords, listWords)))

if __name__ == '__main__':
    main()