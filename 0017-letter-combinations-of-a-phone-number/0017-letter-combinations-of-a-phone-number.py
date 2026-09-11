class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        d = [
            ["2", "3", "4", "5", "6", "7", "8", "9"],
            ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ]
        
        output = []
        
        for j in digits:
            
           
            letters = ""
            for i in range(0, 8):  
                if d[0][i] == j:
                    letters = d[1][i]
                    break
            
            
            f = [k for k in letters]
            
            
            if not output:
                
                output = f
            else:
               
                output_2 = []
                for prev in output:
                    for char in f:
                        output_2.append(prev + char)
                output = output_2  
                
        return output