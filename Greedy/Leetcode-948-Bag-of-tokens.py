from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens)
        maxscore = 0
        score = 0
        while i < j:
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                maxscore = max(maxscore, score)
            else:
                if score > 0:
                    score -= 1
                    power += tokens[j - 1]
                    j -= 1
                    continue
            i += 1
        return maxscore


obj = Solution()
token = [100, 300, 200, 400]
power = 200
print(obj.bagOfTokensScore(token, power))

token = [100]
power = 51
print(obj.bagOfTokensScore(token, power))

tokens = [25, 91]
print(obj.bagOfTokensScore(tokens, power=99))
