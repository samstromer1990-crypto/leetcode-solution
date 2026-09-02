class Solution:
    def romanToInt(self,roman : str) -> int:
        val_map = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C",100), ("XC",90), ("L",50), ("XL",40 ),
            ("X",10 ), ("IX",9 ),( "V",5),( "IV",4),
            ("I",1 )
        ]
        i = 0
        num = 0
        for symbol,val in val_map:
            while i < len(roman) and roman[i : i + len(symbol)] == symbol:
                num += val
                i += len(symbol)
        return num            