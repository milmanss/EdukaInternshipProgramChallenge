def isAnagram(number1, number2):
    list1 = sorted([int(i) for i in str(number1)])
    list2 = sorted([int(i) for i in str(number2)])

    if list1 == list2:
        return True
    else:
        return False

inputNumber1 = int(input())
inputNumber2 = int(input())

if isAnagram(inputNumber1, inputNumber2):
    print("YES")
else:
    print("NO")