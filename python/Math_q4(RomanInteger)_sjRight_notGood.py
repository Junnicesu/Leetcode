class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {}
        dic['I'] = 1  # can be minus
        dic['V'] = 5
        dic['X'] = 10 # can be minus
        dic['L'] = 50
        dic['C'] = 100 # can be minus
        dic['D'] = 500
        dic['M'] = 1000
        dic['IV'] = 4  
        dic['IX'] = 9
        dic['XL'] = 40
        dic['XC'] = 90
        dic['CD'] = 400
        dic['CM'] = 900
        ret = 0
        sz = len(s)
        id = 0
        while id < sz:
            if (s[id] == 'C' or  s[id] == 'X' or s[id] == 'I'):
                if id != sz-1:  
                    subs = s[id] + s[id+1]
                    if subs in ['IV', 'IX','XL', 'XC', 'CD', 'CM']:
                        ret += dic[subs]
                        id+=1
                    else:
                        ret += dic[s[id]]
                else:
                    ret += dic[s[id]]
            else:
                ret += dic[s[id]]
            id+=1
        return ret

'''
No invalid judgement.
No duplicate logics. 
'''