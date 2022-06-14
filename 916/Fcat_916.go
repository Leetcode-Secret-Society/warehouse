import "fmt"

func wordSubsets(words1 []string, words2 []string) []string {
    var words2_union = map[rune]int {}
    for _, word2 := range words2 {
        word2_count := map[rune]int {}
        for _, char := range word2 {
            word2_count[char]++
        }
        for key, value := range word2_count{
            words2_union[key] = Max(words2_union[key], value)
        }
    }
    var result [] string
    for _, word1 := range words1 {
        is_subset := true
        word1_count := map[rune]int {}
        for _, char := range word1 {
            word1_count[char]++
        }

        for key, value := range words2_union {
            if value > word1_count[key] {
                is_subset = false
                break
            }
        }
        if is_subset {
            result = append(result, word1)
        }
    }
    return result
}

func Max(x, y int) int {
    if x < y {
        return y
    }
    return x
}