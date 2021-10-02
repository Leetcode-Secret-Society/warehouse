class Solution:
    def add_kill_count(self, queue, count):
        for x,y in queue:
            self.killable_enemy_count_grid[y][x]+=count
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        self.killable_enemy_count_grid = [[0 for _ in range(width)] for _ in range(height)]
        for y in range(height):
            queue = []
            killable_enemy = 0
            for x in range(width):
                if grid[y][x]=='0':
                    queue.append((x,y))
                elif grid[y][x]=='E':
                    killable_enemy+=1
                else: # wall
                    self.add_kill_count(queue, killable_enemy)
                    queue=[]
                    killable_enemy=0
            self.add_kill_count(queue, killable_enemy)
        #print(self.killable_enemy_count_grid)
        for x in range(width):
            queue = []
            killable_enemy = 0
            for y in range(height):
                if grid[y][x]=='0':
                    queue.append((x,y))
                elif grid[y][x]=='E':
                    killable_enemy+=1
                else: # wall
                    self.add_kill_count(queue, killable_enemy)
                    queue=[]
                    killable_enemy=0
            self.add_kill_count(queue, killable_enemy)
        max_in_row=[]
        for y in range(height):
            max_in_row.append(max(self.killable_enemy_count_grid[y]))
        #print(self.killable_enemy_count_grid)
        return max(max_in_row)
