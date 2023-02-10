func maxDistance(grid [][]int) int {
    queue := [][]int{}
    for y := 0 ; y < len(grid) ; y++{
        for x:= 0 ; x < len(grid) ; x++{
            if grid[y][x] == 1 {
               queue = append(queue, []int{x, y})
            }
        }
    }
    maxDist := 0

    neighbors := [][]int{[]int{1,0}, []int{-1,0}, []int{0,1}, []int{0,-1}}
    for len(queue) != 0 {
       cur := queue[0]
       queue = queue[1:]
       cur_x := cur[0]
       cur_y := cur[1]
       for _, neighbor := range neighbors{
          neighbor_x := neighbor[0]
          neighbor_y := neighbor[1]
          next_x := cur_x + neighbor_x
          next_y := cur_y + neighbor_y
          if next_x >=0 && next_x < len(grid) && next_y >=0 && next_y < len(grid) && grid[next_y][next_x] == 0{
              grid[next_y][next_x] = grid[cur_y][cur_x] + 1
              queue = append(queue, []int{next_x, next_y})
              if grid[next_y][next_x] > maxDist{
                  maxDist = grid[next_y][next_x]
              }
          }

       }
    }
    if maxDist == 0 {
        return -1
    } else{

        return maxDist - 1
    }
}