import math
import numpy as np 
import random as random
import enchant 
from itertools import permutations
          
### NUMBERS CODE ### 
def numberGenerator(big=2,small=4):
    ## must look up what the composistion is 
    bigList = [25,50,75,100]
    smallList = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
     
    target = random.randrange(101,1000,1)
    number_list = []
    i = 0
    while i < small:
        random_index = random.randrange(0,len(smallList),1)
        number_list.append(smallList.pop(random_index))
        i += 1
    j = 0
    while j < big:
        random_index = random.randrange(0,len(bigList),1)
        number_list.append(bigList.pop(random_index))
        j += 1

    return target,number_list

def numberSolver(targetNumber,listNumber):

    target = targetNumber
    targetMet = False
    whileCount = 0
    while targetMet == False:
        buildNumber = 0
        numberList = listNumber.copy()
        listSteps = []
        i = 0
        j = 0 
        while i < len(numberList):
            random_index = random.randrange(0,len(numberList),1)
            number = numberList.pop(random_index)
            #check j if it's first step
            if j == 0:
                operation = 0
                j = 1 
            else:
                operation = random.randrange(0,4,1)

            if operation == 0:
                #add
                stepStr = str(buildNumber)+' '+'plus'+' '+str(number)+ ' = '+str(buildNumber+number)
                listSteps.append(stepStr)
                buildNumber = buildNumber + number
                
            elif operation == 1:
                ## subtract
                stepStr = str(buildNumber)+' '+'minus'+' '+str(number)+ ' = '+str(buildNumber-number)
                listSteps.append(stepStr)
                buildNumber = buildNumber - number

            elif operation == 2:
                ## multiply
                stepStr = str(buildNumber)+' '+'times'+' '+str(number)+ ' = '+str(buildNumber*number)
                listSteps.append(stepStr)
                buildNumber = buildNumber*number

            elif operation == 3:
                ## divide
                #### CURRENTLY DOESN'T ALLOW HOLDING NUMBERS TO THE SIDE ####
                #### AND THEN DIVIDING TWO OTHER NUMBERS IN THE LIST ####
                if buildNumber%number == 0:
                    stepStr = str(buildNumber)+' '+'divided by'+' '+str(number)+ ' = '+str(buildNumber//number)
                    listSteps.append(stepStr)
                    buildNumber = buildNumber//number
                elif number%buildNumber == 0:
                    stepStr = str(number)+' '+'divided by'+' '+str(buildNumber)+ ' = '+str(number//buildNumber)
                    listSteps.append(stepStr)
                    buildNumber = buildNumber//number
                else:
                    # division didn't work, add it back (this could cause it to never end)
                    numberList.append(number)

            if buildNumber == target:
                targetMet = True
                return listSteps
            else:
                pass
            
        whileCount = whileCount + 1
        #print(whileCount)
        if whileCount > 10000:
            return 'took too long'

### LETTERS CODE ###
def letterDistributions():
    letterweights = {
        'E' : 12.49,
        'T' : 9.28,
        'A' : 8.04,
        'O' : 7.64,
        'I' : 7.57,
        'N' : 7.23,
        'S' : 6.51,
        'R' : 6.28,
        'H' : 5.05,
        'L' : 4.07,
        'D' : 3.82,
        'C' : 3.34,
        'U' : 2.73,
        'M' : 2.51,
        'F' : 2.40,
        'P' : 2.14,
        'G' : 1.87,
        'W' : 1.68,
        'Y' : 1.66,
        'B' : 1.48,
        'V' : 1.05,
        'K' : 0.54,
        'X' : 0.23,
        'J' : 0.16,
        'Q' : 0.12,
        'Z' : 0.09,
        }

    # multiply letter weights by 12 to get the distribution
    letterDistribution = {}
    for key in letterweights:
        number = letterweights[key]
        # multiply by 24 and round down
        number = math.floor(number*24)
        letterDistribution[key] = number

    # create list of letter distributions
    # splitting bettwen vowel and consonant
    vowelList = []
    consonantList = []
    vowels = ['A','E','I','O','U']

    for key in letterDistribution:
        if key in vowels:
            while letterDistribution[key] > 0:
                vowelList.append(key)
                letterDistribution[key] = letterDistribution[key] - 1
                
        else:
            while letterDistribution[key] > 0:
                consonantList.append(key)
                letterDistribution[key] = letterDistribution[key] - 1
    return vowelList,consonantList
    
def lettersGenerator(vowel=3,consonant=6):
    vowelList, consonantList = letterDistributions()
    listNineLetters = []
    i = 0
    while i < vowel:
        random_index = random.randrange(0,len(vowelList),1)
        listNineLetters.append(vowelList.pop(random_index))
        i = i + 1
    j = 0
    while j < consonant:
        random_index = random.randrange(0,len(consonantList),1)
        listNineLetters.append(consonantList.pop(random_index))
        j = j + 1
    random.shuffle(listNineLetters)
    return listNineLetters


def all_permutations_substrings(a_str):
    # helper function
    return (
        ''.join(item)
        for length in range(1, len(a_str)+1)
        for item in permutations(a_str, length))
        
def wordSolver(lettersList,numberSolutions=20):
    d = enchant.Dict("en_US")
    string = ''
    for letter in lettersList:
        string = string + letter

    allPermutationsNoDupes = set(all_permutations_substrings(string))
    listWords = []
    for string in allPermutationsNoDupes:
        if d.check(string) == True:
            listWords.append(string)
    #can order by length later
    sorted_list = sorted(listWords, key=len, reverse=True)
    return sorted_list[:numberSolutions]

if __name__=='__main__':
    letters = ['N','O','O','N','E','F','A','R','T']
    words = wordSolver(letters)
    for word in words:
        print(word)


#### NOTES ####
# dictionary is including proper nouns and acronyms
# MUST CHECK pyenchant documentation 
# not using the offical countdown distribution for letters and numbers
# need to see if I can find that online

    
    
