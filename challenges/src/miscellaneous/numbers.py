import functools

def longDivision(numerator, denominator):
    print(numerator, denominator)
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



