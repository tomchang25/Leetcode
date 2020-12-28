# %%
import math


def decomb(val):
    r = []
    size = int(math.log10(val))
    for _ in range(size):
        r.append(val % 10)
        val = int(val / 10)

    r.append(val)
    r.reverse()
    return r


def comb(ls):
    r = 0
    for i in range(0, len(ls)):
        r *= 10
        r += ls[i]

    return r


def swap(ls, a, b):
    t_ls = ls.copy()

    t_ls[a] = ls[b]
    t_ls[b] = ls[a]

    return t_ls


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        ls = decomb(n)

        small_key = -1
        t = ls[-1]
        for i in range(len(ls) - 1, -1, -1):
            if ls[i] > t:
                t = ls[i]
            elif ls[i] < t:
                small_key = i
                break

        if small_key < 0:
            return -1

        swap_key = small_key + 1
        for i in range(swap_key, len(ls)):
            if ls[i] < ls[swap_key] and ls[i] > ls[small_key]:
                swap_key = i

        rarr = swap(ls, small_key, swap_key)
        rarr[small_key + 1 :] = sorted(rarr[small_key + 1 :])

        final = comb(rarr)

        if final < 2 ** 31 - 1:
            return final
        else:
            return -1


test = 2 ** 31 - 115
print(test, Solution().nextGreaterElement(test))
# 12443322
# 13222344

# 230412
# %%
