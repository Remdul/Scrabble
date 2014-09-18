# Vowels      = 2
# Constinents = 1
# Extra bonus points
#6 extra points for 3 vowels in the row + normal values
#10 extra points if any sequence of every 4th letter has a run
#download a word list - find anagrams in said list



import re

def wordScan(unscoredWord):
    totalScore = 0
    chCount = 0
    for i in range(len(unscoredWord)):
        wordCh = unscoredWord[i]
        if re.search("[aeiou]", wordCh) is not None:
            if chCount % 5 == 4:
                totalScore = totalScore + 6
            else:
                totalScore = totalScore + 2
        elif re.search("[bcdfghjklmnpqrstvwxyz]", wordCh) is not None:
            if chCount % 5 == 4:
                totalScore = totalScore + 3
            else:
                totalScore = totalScore + 1
        else:
            print("This is not a scorable character")

        chCount = chCount + 1
    return totalScore

def main():
    prompt = "Which word would you like to score: "
    unscoredWord = raw_input(prompt)
    finalscore = wordScan(unscoredWord)
    print (unscoredWord, finalscore)

if __name__ == '__main__':
    main()
