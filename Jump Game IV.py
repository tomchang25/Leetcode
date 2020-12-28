# %%
from typing import List
from operator import itemgetter, attrgetter


class Solution:
    def minJumps(self, _arr: List[int]) -> int:
        hash = {}
        prev_x = None
        rep_counter = 0
        arr = []
        for x in _arr:
            if prev_x is not None and prev_x == x:
                if rep_counter < 1:
                    rep_counter += 1
                    arr.append(x)
                else:
                    continue
            else:
                arr.append(x)

            if x not in hash:
                hash[x] = []

            hash[x].append(len(arr) - 1)
            prev_x = x

        print(hash)
        print(arr)
        # for key in hash.keys():
        #     hash[key] = sorted(hash[key], reverse=True)

        q = []
        visited = [False] * len(arr)

        visited[0] = True
        q.append((0, 0))
        while len(q) > 0:
            key, distance = q.pop(0)
            print(key)

            if key + 1 < len(arr) and not visited[key + 1]:
                q.append((key + 1, distance + 1))
                visited[key + 1] = True

            if key - 1 > 0 and not visited[key - 1]:
                q.append((key - 1, distance + 1))
                visited[key - 1] = True

            for child in hash[arr[key]]:
                if child == key:
                    continue

                if not visited[child]:
                    visited[child] = True
                    q.append((child, distance + 1))

                    if child == len(arr) - 1:
                        return distance + 1

            if key == len(arr) - 1:
                return distance


if __name__ == "__main__":
    S = Solution()
    test1 = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    test2 = [
        51,
        64,
        -15,
        58,
        98,
        31,
        48,
        72,
        78,
        -63,
        92,
        -5,
        64,
        -64,
        51,
        -48,
        64,
        48,
        -76,
        -86,
        -5,
        -64,
        -86,
        -47,
        92,
        -41,
        58,
        72,
        31,
        78,
        -15,
        -76,
        72,
        -5,
        -97,
        98,
        78,
        -97,
        -41,
        -47,
        -86,
        -97,
        78,
        -97,
        58,
        -41,
        72,
        -41,
        72,
        -25,
        -76,
        51,
        -86,
        -65,
        78,
        -63,
        72,
        -15,
        48,
        -15,
        -63,
        -65,
        31,
        -41,
        95,
        51,
        -47,
        51,
        -41,
        -76,
        58,
        -81,
        -41,
        88,
        58,
        -81,
        88,
        88,
        -47,
        -48,
        72,
        -25,
        -86,
        -41,
        -86,
        -64,
        -15,
        -63,
    ]

    test3 = [7, 7, 7, 7, 1]
    print(S.minJumps(test3))


# %%
