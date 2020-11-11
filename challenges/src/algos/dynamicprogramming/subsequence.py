

def longestIncreasingSubsequenceLength(sequence):
    lis = [1]*len(sequence)
    maxEnc = 0
    for i in range(len(sequence)):
        for j in range(i):
            if sequence[j] < sequence[i] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1
        maxEnc = max(maxEnc, lis[i])
    return maxEnc
