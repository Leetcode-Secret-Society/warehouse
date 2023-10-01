class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur_dic = self.trie
        for c in word:
            if c not in cur_dic:
                cur_dic[c] = {}
            cur_dic["start_with_count"] = cur_dic.get("start_with_count", 0) + 1
            cur_dic = cur_dic[c]
        cur_dic["count"] = cur_dic.get("count", 0) + 1
        cur_dic["start_with_count"] = cur_dic.get("start_with_count", 0) + 1

    def countWordsEqualTo(self, word: str) -> int:
        cur_dic = self.trie
        for c in word:
            if c not in cur_dic:
                return 0
            cur_dic = cur_dic[c]
        return cur_dic.get("count", 0)

    def countWordsStartingWith(self, prefix: str) -> int:
        cur_dic = self.trie
        for c in prefix:
            if c not in cur_dic:
                return 0
            cur_dic = cur_dic[c]
        return cur_dic.get("start_with_count", 0)

    def erase(self, word: str) -> None:
        def check_word_in_trie(cur_dic, index):
            if word[index] in cur_dic:
                if index == len(word) - 1:
                    if cur_dic[word[index]].get("count", 0):
                        cur_dic[word[index]]["count"] -= 1
                        cur_dic[word[index]]["start_with_count"] -= 1
                        return True
                    else:
                        return False
                if check_word_in_trie(cur_dic[word[index]], index + 1):
                    cur_dic[word[index]]["start_with_count"] -= 1
                    return True
                else:
                    return False
            else:
                return False

        check_word_in_trie(self.trie, 0)

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("apple")
param_2 = obj.countWordsEqualTo("apple")
param_3 = obj.countWordsStartingWith("app")
obj.erase("apple")
param_4 = obj.countWordsEqualTo("apple")
param_5 = obj.countWordsStartingWith("app")
obj.erase("apple")
param_6 = obj.countWordsStartingWith("app")