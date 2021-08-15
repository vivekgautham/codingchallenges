
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        days = sorted(set(bloomDay))
        dayToBloomed = {}
        prevList = []
        for i, e in enumerate(bloomDay):
            dayToBloomed.setdefault(e, set()).add(i+1)

        #print(dayToBloomed)

        def _maxConsecInts(st):
            d = {}
            res = 0
            mn = sys.maxsize
            for e in st:
                if e not in d:
                    l = d.get(e-1, 0)
                    r = d.get(e+1, 0)
                    cur = l + r + 1
                    if cur > res:
                        res = max(res, cur)
                        mn = e
                    for x in [e-l, e, e+r]:
                        d[x] = cur
            while mn-1 in st:
                mn = mn-1
            return res, mn

        #print(_maxConsecInts({1, 3, 5, 7, 9, 10}))
        #days = []
        ans = -1
        s = set()
        for day in days:
            s |= dayToBloomed[day]
            #print(s)
            print("Day ", day)
            while True:
                mc, mn = _maxConsecInts(s)
                print(mc, mn)

                if mc//k > 0:
                    bs = (mc//k)
                    m -= bs
                    ad = bs*k
                    for item in range(mn, mn+ad):
                        s.remove(item)
                else:
                    break

            print(m)
            if m <= 0:
                ans = day
                break
            #print("After Remov ", s)
        return ans



