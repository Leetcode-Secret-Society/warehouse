class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        previous_status = 'L'
        previous_index = -1
        result_dominoes = []
        for i, d in enumerate(dominoes):
            length = i-previous_index+1
            if d == 'L':
                if previous_status == 'L':
                    result_dominoes.extend(['L']*(length-1))
                elif previous_status == 'R':
                    if length % 2 == 0:
                        result_dominoes.extend(['R']*(length//2-1))
                        result_dominoes.extend(['L']*(length//2))
                    else:
                        result_dominoes.extend(['R']*(length//2-1))
                        result_dominoes.append('.')
                        result_dominoes.extend(['L']*(length//2))
                #print(i)
                #print(previous_index)
                #print(result_dominoes)
            elif d == 'R':
                if previous_status == 'L':
                    result_dominoes.extend(['.']*(length-2))
                    result_dominoes.append('R')
                elif previous_status == 'R':
                    result_dominoes.extend(['R']*(length-1))
                #print(i)
                #print(previous_index)
                #print(result_dominoes)
            else:
                continue
            
            previous_status = d
            previous_index = i
        
        length = len(dominoes) - previous_index
        if previous_status in ['L', '.']:
            result_dominoes.extend(['.']*(length-1))
        else:
            result_dominoes.extend(['R']*(length-1))
            
        return "".join(result_dominoes)
                
            
            
