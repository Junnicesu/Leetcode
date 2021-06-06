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
            if id == sz -1:
                ret += dic[s[id]]
            else:
                if s[id] + s[id+1] in ['IV', 'IX','XL', 'XC', 'CD', 'CM']:
                    ret += dic[s[id]+s[id+1]]
                    id+=1
                else:
                    ret += dic[s[id]]
            id+=1
        return ret

'''
No invalid judgement.
No duplicate logics.  --- little improved comparing to the notGood1.py
'''