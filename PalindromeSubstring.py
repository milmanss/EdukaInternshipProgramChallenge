import Palindrome

def makeAllPalindromeSubstring(string):
    listOfPalindromeSubstring = list()

    for i in range(len(string)):
        substring = string[i]
        metadataSubstring = [substring, i, i]
        listOfPalindromeSubstring.append(metadataSubstring)
        for j in range(i + 1, len(string)):
            substring += string[j]
            if Palindrome.isPalindrome(substring):
                metadataSubstring = [substring, i, j]
                listOfPalindromeSubstring.append(metadataSubstring)

    return listOfPalindromeSubstring

inputString = input()

listOfPalindromeSubstring = makeAllPalindromeSubstring(inputString)

longest = listOfPalindromeSubstring[0]
for palindromeSubstring in listOfPalindromeSubstring:
    if len(palindromeSubstring[0]) > len(longest[0]):
        longest = palindromeSubstring

print("%d %d" % (longest[1], longest[2]))