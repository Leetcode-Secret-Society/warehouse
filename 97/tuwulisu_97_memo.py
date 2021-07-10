class Solution:
    def do_isInterleave(self, s_index_tuple):
        if s_index_tuple in self.deadend_set:
            return False
        s1_index, s2_index, s3_index = s_index_tuple
        while s3_index != len(self.s3):
            if s1_index == len(self.s1):
                if self.s2[s2_index] == self.s3[s3_index]:
                    s2_index+=1
                    s3_index+=1
                    continue
                else:
                    return False
            
            if s2_index == len(self.s2):
                if self.s1[s1_index] == self.s3[s3_index]:
                    s1_index+=1
                    s3_index+=1
                    continue
                else:
                    return False
            
            if self.s1[s1_index] == self.s2[s2_index] == self.s3[s3_index]:
                self.save_points.append((s1_index, s2_index+1, s3_index+1))
                s1_index+=1
                s3_index+=1
            elif self.s1[s1_index] == self.s3[s3_index]:
                s1_index+=1
                s3_index+=1
            elif self.s2[s2_index] == self.s3[s3_index]:
                s2_index+=1
                s3_index+=1
            else:
                return False
        else:
            return True
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.save_points = [(0,0,0)]
        self.deadend_set = set()
        while self.save_points:
            resume_point = self.save_points.pop()
            if self.do_isInterleave(resume_point):
                return True
            else:
                self.deadend_set.add(resume_point)
        else:
            return False
        
                
        
