def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}

        for word in strs:
            
            sorted_word = ''.join(sorted(word))
            if sorted_word in dict:
                 dict[sorted_word].append(word)
            else:
                 dict[sorted_word] = [word]
        
        for key, val in dict.items():
            print(key, val)
        
        return list(dict.values())
        
strs = ["eat","tea","tan","ate","nat","bat"]
list_val = groupAnagrams(strs)
print(list_val)