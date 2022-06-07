import "fmt"

func corpFlightBookings(bookings [][]int, n int) []int {
    var result = make([]int, n + 1)
    for _, booking := range bookings{
        start, end, seats := booking[0], booking[1], booking[2]
        result[start - 1] += seats
        result[end] -= seats
    }
    for i := 1; i < n; i++{
        result[i] += result[i-1]
    }
        
    return result[:n]
}