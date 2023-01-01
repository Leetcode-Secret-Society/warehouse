class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counters = defaultdict(int)
        for n in arr:
            counters[n]+=1
        counters_list = [(n, count) for n, count in counters.items()]
        length = len(counters_list)
        ans = 0
        walked_pairs = set()
        for i in range(length):
            for j in range(i, length):
                n1 = counters_list[i][0]
                n2 = counters_list[j][0]
                added_number = n1 + n2
                n3 = target - added_number
                c1 = counters_list[i][1]
                c2 = counters_list[j][1]
                if n3 in counters:
                    c3 = counters[n3]
                    walked_pair = tuple(sorted([n1, n2, n3]))
                    if walked_pair in walked_pairs:
                        continue
                    else:
                        walked_pairs.add(walked_pair)
                    #print(counters_list[i], counters_list[j], (n3, c3))
                    if n1!=n2 and n2!=n3:
                        ans+= counters[n3] * counters_list[i][1] * counters_list[j][1]
                    elif n1 == n2 and n2 == n3:
                        if c1 >= 3 and c2 >=3 and c3 >=3:
                            ans+= math.comb(c1,3)
                    elif c1>=2 and c2>=2 and n1 == n2:
                        ans+= c3 * math.comb(c1,2)
                    elif c2>=2 and c3>=2 and n2 == n3:
                        ans+= c1 * math.comb(c2,2)
                    elif c1>=2 and c3>=2 and n1 == n3:
                        ans+= c2 * math.comb(c1,2)

        return ans % 1000000007
