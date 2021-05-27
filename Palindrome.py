def isPalindrome(number):
    stringNumber = str(number)
    lengthString = len(stringNumber)
    check = lengthString // 2

    forward = 0
    backward = lengthString - 1
    while check != 0:
        if stringNumber[forward] != stringNumber[backward]:
            return False
        else:
            forward += 1
            backward -= 1
            check -= 1
    return True

inputNumber = int(input())

if isPalindrome(inputNumber):
    print("YES")
else:
    print("NO")