class Solution {
    func successfulPairs(_ spells: [Int], _ potions: [Int], _ success: Int) -> [Int] {
        let sortedPotions = potions.sorted()

        func checkSpell(_ spell: Int, _ success: Int) -> Int {
            var left = 0
            var right = sortedPotions.count - 1
            while left <= right {
                let mid = Int((left+right)/2)
                let potionedSpell = sortedPotions[mid] * spell
                // print((sortedPotions[mid], potionedSpell))
                // if potionedSpell == success {
                //     return mid
                // }
                // else if potionedSpell < success {
                if potionedSpell < success {
                    left = mid + 1
                }
                else {
                    right = mid - 1
                }
            }
            return left
        }
        var result = [Int]()
        for spell in spells {
            // print("sp:\(spell)")
            // print(potions.count - checkSpell(spell, success))
            result.append(potions.count - checkSpell(spell, success))
        }

        return result
    }
}
