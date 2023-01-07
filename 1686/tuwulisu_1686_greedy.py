class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        taken_stone_index = set()
        stones = [v1+v2 for v1, v2 in zip(aliceValues, bobValues)]
        stones = [(i,v) for i, v in enumerate(stones)]
        stones.sort(key=lambda v: v[1], reverse=True)
        alice_score = 0
        bob_score = 0
        for i, stone in enumerate(stones):
            if i%2==0:
                alice_score+=aliceValues[stone[0]]
            else:
                bob_score+=bobValues[stone[0]]
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0
