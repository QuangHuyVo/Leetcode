class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1

        word = [''] * L
        fixed = [False] * L

        # Step 1: apply all T constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    ch = str2[j]
                    if word[pos] != '' and word[pos] != ch:
                        return ""
                    word[pos] = ch
                    fixed[pos] = True

        # Fill remaining positions with 'a'
        for i in range(L):
            if word[i] == '':
                word[i] = 'a'

        # Step 2: satisfy all F constraints
        for i in range(n):
            if str1[i] == 'F':
                # Check whether current window equals str2
                equal = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        equal = False
                        break

                if not equal:
                    continue

                # Need to break this equality
                changed = False
                for j in range(m - 1, -1, -1):
                    pos = i + j
                    if not fixed[pos]:
                        # Change to smallest different character
                        word[pos] = 'a' if str2[j] != 'a' else 'b'
                        changed = True
                        break

                if not changed:
                    return ""

        return ''.join(word)
        