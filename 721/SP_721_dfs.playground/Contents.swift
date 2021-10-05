class Solution {
    func accountsMerge(_ accounts: [[String]]) -> [[String]] {
        var map = [String:[Int]]()
        for (accountIndex,account) in accounts.enumerated() {
            for i in 1..<account.count {
                let mail = account[i]
                var mailToIndexMap = map[mail] ?? [Int]()
                mailToIndexMap.append(accountIndex)
                map[mail] = mailToIndexMap
            }
        }
        var accountVisited = [Int:Bool]()
        func dfs(_ accountIndex: Int,_ mails: [String]) -> [String] {
            if accountVisited[accountIndex] == true {
                return mails
            }
            accountVisited[accountIndex] = true
            var mails = mails
            let account = accounts[accountIndex]
            for i in 1..<account.count {
                let mail = account[i]
                if mails.contains(mail) {
                    continue
                }
                mails.append(mail)
                for neighborIndex in map[mail] ?? [] {
                    mails = dfs(neighborIndex, mails)
                }
            }
            return mails
        }
        
        var result = [[String]]()
        for (accountIndex, account) in accounts.enumerated() {
            if accountVisited[accountIndex] == true {
                continue
            }
            let name = account.first!
            let emails = dfs(accountIndex, [String]())
            var aResult = [String]()
            aResult.append(name)
            aResult.append(contentsOf: emails.sorted())
            result.append(aResult)
        }
//        print(map)
        return result
    }
}
let result = Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
])

print(result)
