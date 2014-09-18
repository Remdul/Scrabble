# Vowels      = 2
# Constinents = 1
# Extra bonus points
#6 extra points for 3 vowels in the row + normal values
#10 extra points if any sequence of every 4th letter has a run
#download a word list - find anagrams in said list

from __future__ import print_function

import re

def wordScan(unscoredWord):
    totalScore = 0
    chCount = 0
    for i in range(len(unscoredWord)):
        wordCh = unscoredWord[i]
        if re.search("[aeiou]", wordCh) is not None:
            if chCount % 5 == 4:
                totalScore += 6
            else:
                totalScore += 2
        elif re.search("[bcdfghjklmnpqrstvwxyz]", wordCh) is not None:
            if chCount % 5 == 4:
                totalScore += 3
            else:
                totalScore += 1
        else:
            print("This is worth no points.")

        chCount += 1
    pattern = re.compile("[aeiou]{3}")
    listMatches = pattern.findall(unscoredWord)
    if pattern.search(unscoredWord) is not None:
        for j in range(len(listMatches)):
            totalScore += 6

    chCount = 0
    runLetters = []
    for k in range(len(unscoredWord)):
        wordCh = unscoredWord[k]
        if chCount % 4 == 3:
            runLetters.append(wordCh)
        chCount += 1

    gotRun = False
    for l in range(len(runLetters)):
        for m in range(1, len(runLetters)):
            if runLetters[l] != runLetters[m]:
                break;
            else:
                gotRun = True

    if gotRun == True:
        print("Got a Run!")
        totalScore += 10

    return totalScore

def showHelp():
    print ("\nVowels = 2")
    print ("Consts = 1")
    print ("-------------------------")
    print ("-Additional Bonus Points-")
    print ("-------------------------")
    print ("Every 5th letter is worth 3x")
    print ("3 consecutive vowels is +6")
    print ("If you can match every 4th letter, +10")
    print ("\n\n")

def main():
    showHelp()
    prompt = "Which word would you like to score: "
    unscoredWord = raw_input(prompt)
    finalscore = wordScan(unscoredWord)
    print (unscoredWord, " == ", finalscore)

if __name__ == '__main__':
    main()
