from __future__ import print_function

import csv

def importFile(listWords):
    with open('words.csv', 'rb') as csvfile:
        wordReader = csv.reader(csvfile)
        for row in wordReader:
            row = "".join(row)
            listWords.append(row)

def main():
    listWords = []
    sortedWords = []
    importFile(listWords)
    listWords.sort()

    for i in range(len(listWords)):
        sortedWords.append(''.join(sorted(listWords[i])))

#    sortedWords.sort()
    for i in range(len(sortedWords)):
        print(sortedWords[i])
        print(listWords[i])


if __name__ == '__main__':
    main()