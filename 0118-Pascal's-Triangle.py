from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1],]
        result = [[1], [1,1]]
        for i in range(3, numRows+1):
            prev_row = result[-1]
            row = [1, 1]
            for j in range(1, i-1):
                row.insert(j, (prev_row[j-1] + prev_row[j]))
            result.append(row)
        return result
    
