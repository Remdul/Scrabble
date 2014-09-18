from __future__ import print_function

import csv

def importFile(listWords):
    with open('words.csv', 'rb') as csvfile:
        wordReader = csv.reader(csvfile)
        for row in wordReader:
            row = "".join(row)
            listWords.append(row)

def find_dup(sortedWords, listWords):
    for i in range(len(sortedWords)):
        for j in range(0, max(range(len(sortedWords))) - 1):
            if sortedWords[i] == sortedWords[j] and i != j:
                print ('I= {:4d} J={:4d} Sorted= {:14s} Word= {:14s} Matches = {:14s}'.format(i, j, sortedWords[i], listWords[i], listWords[j]))

def main():
    listWords = []
    sortedWords = []
    importFile(listWords)
    listWords.sort()

    for i in range(len(listWords)):
        sortedWords.append(''.join(sorted(listWords[i])))

    print ("Anagram words: \n" , list(find_dup(sortedWords, listWords)))

if __name__ == '__main__':
    main()
