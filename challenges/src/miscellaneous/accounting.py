
from sys import maxsize

def taxesOwed(income):
    taxBracket = [
        (9525, 0.1),
        (38700, 0.12),
        (82500, 0.22),
        (157500, 0.24),
        (200000, 0.32),
        (500000, 0.35),
        (maxsize, 0.37)
    ]
    taxes = 0.0
    idx = 0
    while income:
        prevBr = taxBracket[idx-1] if idx > 0 else (0, 0)
        curBr = taxBracket[idx]
        curBrAmt = float(curBr[0] - prevBr[0])
        if income > curBrAmt:
            taxes += curBrAmt * curBr[1]
            income -= curBrAmt
            idx += 1
        else:
            taxes += income * curBr[1]
            income = 0
    return taxes
