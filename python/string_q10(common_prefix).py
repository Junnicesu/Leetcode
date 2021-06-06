class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "" 
        
        prefix = ""        
        for id,ch in enumerate(strs[0]):            
            isPrefix = True
            for s in strs[1:]:
                if id > len(s)-1:
                    isPrefix = False
                    break
                else:
                    if ch == s[id]:
                        pass
                    else:
                        isPrefix = False
                        break
            if isPrefix:
                prefix += ch
            else:
                break  //!!sj forget
        return prefix