# https://leetcode.com/problems/decode-the-slanted-ciphertext/

def decodeCiphertext(self, encodedText: str, rows: int) -> str:
    n = len(encodedText)
    cols = n // rows
    a = []
    
    for i in range(cols):
        r, c = 0, i

        while r < rows and c < cols:
            a.append(encodedText[r * cols + c])
            r += 1
            c += 1
    
    return "".join(a).rstrip() # (199 ms)