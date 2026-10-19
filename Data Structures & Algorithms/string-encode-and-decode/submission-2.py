class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            hash_position = s.find("#", i)
            length = int(s[i:hash_position])
            start = hash_position + 1
            piece = s[start: start + length]

            decoded.append(piece)

            i = start + length

        return decoded
        


#class Solution:
    #def encode(self, strs: List[str]) -> str:
         # build up a result string
        # for each string in strs, add: length + "#" + string
        #pass