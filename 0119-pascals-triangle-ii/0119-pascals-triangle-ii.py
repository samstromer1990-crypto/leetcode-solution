class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        output = [[1]]

        rowIndex += 1
        
        if rowIndex >= 2:
            output.append([1, 1])
            
        while len(output) < rowIndex:
            prev_row = output[-1]  
            new_row = [1]          
            
            for j in range(len(prev_row) - 1):
                Sum = prev_row[j] + prev_row[j + 1]
                new_row.append(Sum)
                
            new_row.append(1)      
            output.append(new_row)
            
        return output[-1]