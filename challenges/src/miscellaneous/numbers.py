import functools

def longDivision(numerator, denominator):
    quotient = numerator//denominator
    remainder = numerator%denominator
    result = '{q}.{r}'
    rl = []
    seen = []
    seenIdx = None
    while remainder:
        remainder *= 10
        if remainder not in seen:
            seen.append(remainder)
        else:
            seenIdx = seen.index(remainder)
            break

        rl.append(str(remainder//denominator))
        remainder = remainder%denominator
    if seenIdx is not None:
        result = result.format(q=quotient, r=''.join(rl[:seenIdx]) + '(' + ''.join(rl[seenIdx:]) + ')' )
    else:
        result = result.format(q=quotient, r=''.join(rl))
    return result

def gcd(a, b):
    if a > b:
        gcd(b, a)
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

def gcdInBulk(numbers):
    return functools.reduce(gcd, numbers[1:], numbers[0])

def intToRoman(number):
    baseNumbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    baseRomans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = len(baseNumbers)-1
    res = ''
    while number:

        div = number//baseNumbers[i]
        number = number%baseNumbers[i]

        while div:
            res += baseRomans[i]
            div -= 1
        i -= 1

    return res


def romanToInt(romanNumber):
    romanToInt = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    prevVal = 0
    res = 0
    for i in range(len(romanNumber)-1, -1, -1):
        if romanToInt[romanNumber[i]] >= prevVal:
            res += romanToInt[romanNumber[i]]
        else:
            res -= romanToInt[romanNumber[i]]
        prevVal = romanToInt[romanNumber[i]]
    return res


def highestPossibleNumberFromArray(arr):

    def _digit(x, y):
        x = str(x)
        y = str(y)
        return int(x+y) - int(y+x)


    arr.sort(key=functools.cmp_to_key(_digit), reverse=True)
    return int(''.join(map(str, arr)))




def isNumber(s: str) -> bool:

    def _checkInt(inte):
        if not inte: return False
        signCt = 0
        numCt = 0
        i = 0
        while i < len(inte) and inte[i] in ['+', '-']:
            signCt += 1
            i += 1
        if signCt > 1: return False
        while i < len(inte) and ord('0') <= ord(inte[i]) <= ord('9'):
            numCt += 1
            i += 1
        return (numCt > 0) and (numCt + signCt) == len(inte)


    def _checkDec(dec):
        if not dec: return False
        signCt = 0
        dotCt = 0
        digBeforeDot = 0
        digAfterDot = 0
        i = 0
        while i < len(dec) and dec[i] in ['+', '-']:
            signCt += 1
            i += 1
        if signCt > 1: return False
        while i < len(dec) and ord('0') <= ord(dec[i]) <= ord('9'):
            digBeforeDot += 1
            i += 1
        while i < len(dec) and dec[i] == '.':
            dotCt += 1
            i += 1
        if dotCt > 1: return False
        while i < len(dec) and ord('0') <= ord(dec[i]) <= ord('9'):
            digAfterDot += 1
            i += 1
        return ((signCt + dotCt + digBeforeDot + digAfterDot) == len(dec)) and (digBeforeDot or digAfterDot)

    s = s.lower()
    comp = s.split('e')
    #print(comp)
    if len(comp) in [1, 2]:
        decOrInt = comp[0]
        decOrIntCheck = (_checkDec(decOrInt) or _checkInt(decOrInt))
        #print(decOrIntCheck, _checkDec(decOrInt), _checkInt(decOrInt))
        if len(comp) == 2:
            inte = comp[1]
            return _checkInt(inte) and decOrIntCheck
        else:
            return decOrIntCheck
    else:
        return False
