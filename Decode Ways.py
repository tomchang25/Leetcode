# %%
class Solution:
    def numDecodings(self, s: str) -> int:

        if s == "0":
            return 0
        dp = [1] + [-1] * 100
        for i in range(len(s)):
            code = s[: i + 1]
            # print(s, code, dp)
            ret = 0

            if dp[len(code)] > 0:
                return dp[len(code)]

            if code[-1] != "0":
                ret += dp[len(code) - 1]

            if int(code[-2:]) <= 26 and int(code[-2:]) >= 10:
                ret += dp[len(code) - 2]

            dp[len(code)] = ret

        return dp[len(s)]


test1 = "12620"
test2 = "12345162718"
test3 = "10"

print(Solution().numDecodings("2101"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("10"))
# print(dp)


# %%
