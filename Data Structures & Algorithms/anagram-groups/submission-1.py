class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        # brute force: timeout crash
        # for word in strs:
        #     sorted_word = sorted(word)
        #     found = False

        #     for group in result:
        #         if sorted(group[0]) == sorted_word:
        #             group.append(word)
        #             found = True
        #             break
        #     if not found:
        #         result.append([word])
        
        groups = {}
        for word in strs:
            count = [0]*26
            for char in word:
                position = ord(char) - ord('a')
                count[position] += 1
            sign = tuple(count)

            if sign in groups:
                groups[sign].append(word)
            else:
                groups[sign] = [word]


        return list(groups.values())