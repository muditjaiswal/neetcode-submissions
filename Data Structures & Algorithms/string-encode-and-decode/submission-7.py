class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] != "#":
                j += 1
            word_len = int(s[i: j])
            i = j + 1
            j = i + word_len
            decoded.append(s[i: j])
            i = j
        
        return decoded
