class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        print(f"{len(sentence1)=}, {len(sentence2)=}")
        if len(sentence1) != len(sentence2):
            return False
        mixed = defaultdict(set)
        for i in sentence1:
            mixed[i].add(i)
        for i in sentence2:
            mixed[i].add(i)
        
        for pairs in similarPairs:
            mixed[pairs[0]].add(pairs[1])
            mixed[pairs[1]].add(pairs[0])
            
        for i in range(len(sentence2)):
            if not sentence1[i] in mixed[sentence2[i]]:
                return False
        return True
