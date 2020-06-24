'''Kevin and Stuart want to play the 'The Minion Game'.
Game Rules:
Both players are given the same string,S .
Both players have to make substrings using the letters of the string S .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring:
A player gets +1 point for each occurrence of the substring in the string S .
For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
For better understanding, see the image below:
https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png
Your task is to determine the winner of the game and their score.
Input Format:
A single line of input containing the string S.
Note: The string  will contain only uppercase letters:[A-Z] .
Output Format:
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
Sample Input:
BANANA
Sample Output:
Stuart 12'''
#My Code
def minion_game(string):
    # your code goes here BANANA#copied form discussion
    vowel='AEIOU'
    kevinvowelpoints=0
    stuartconsonantpoints=0
    for i in range(len(string)):
        if string[i] in vowel:
            #Eg:For i=1 we are sure that there is an occurrence for all the substrings that follow , hence below code
            kevinvowelpoints=kevinvowelpoints+len(string)-i
        else:
            stuartconsonantpoints=stuartconsonantpoints+len(string)-i
    if kevinvowelpoints>stuartconsonantpoints:
        print('Kevin',kevinvowelpoints)
    elif kevinvowelpoints<stuartconsonantpoints:
        print('Stuart',stuartconsonantpoints)
    else:
        print('Draw')



#MY CODE
    '''vowel='AEIOU'
    vowelcounter=0
    consonantcounter=0
    temp=0
    temp1=0
    stuartpoints=0
    kevinpoints=0
    length=len(string)
    for i in range(length):
        if string[i] in vowel:
            vowelcounter=vowelcounter+1
            S=[string[i:j] for j in range(i,length+1)]
            temp=temp+len(S)
    kevinpoints=kevinpoints+temp-vowelcounter
    for i in range(length):
        if string[i] not in vowel:
            consonantcounter=consonantcounter+1
            S=[string[i:j] for j in range(i,length+1)]
            temp1=temp1+len(S)
    stuartpoints=stuartpoints+temp1-consonantcounter
    if kevinpoints>stuartpoints:
        print('Kevin',kevinpoints)
    elif kevinpoints<stuartpoints:
        print('Stuart',stuartpoints)
    else:
        print('Draw')'''
if __name__ == '__main__':
    s = input()
    minion_game(s)
