# 443. String Compression
# https://leetcode.com/problems/string-compression?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def compress(self, chars):
        last = chars[0]
        idx = 0
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i] == last:
                cnt += 1
            else:
                chars[idx] = last
                idx += 1
                if cnt > 1:
                    d = 1
                    while d <= cnt:
                        d *= 10
                    d //= 10
                    while d > 0:
                        chars[idx] = str(cnt // d)
                        idx += 1
                        cnt %= d
                        d //= 10
                cnt = 1
                last = chars[i]

        chars[idx] = last
        idx += 1
        if cnt > 1:
            d = 1
            while d <= cnt:
                d *= 10
            d //= 10
            while d > 0:
                chars[idx] = str(cnt // d)
                idx += 1
                cnt %= d
                d //= 10

        return idx


# 정답으로 처리되지만 문제 조건을 만족하지 않았음
# You must write an algorithm that uses only constant extra space.
# class Solution(object):
#     def compress(self, chars):
#         ans = [chars[0]]
#         cnt = 1
#         for c in chars[1:]:
#             if c == ans[-1]:
#                 cnt += 1
#             else:
#                 if cnt > 1:
#                     cnt_str = str(cnt)
#                     for cntc in cnt_str:
#                         ans.append(cntc)
#                 ans.append(c)
#                 cnt = 1

#         if cnt > 1:
#             cnt_str = str(cnt)
#             for cntc in cnt_str:
#                 ans.append(cntc)
#         for i in range(len(ans)):
#             chars[i] = ans[i]
#         return len(ans)


# class Solution(object):
#     def compress(self, chars):
#         read = write = 0
#         length = len(chars)

#         while read < length:
#             char = chars[read]
#             group_start = read

#             while read < length and chars[read] == char:
#                 read += 1

#             count = read - group_start
#             chars[write] = char
#             write += 1

#             if count > 1:
#                 divisor = 1
#                 while divisor <= count // 10:
#                     divisor *= 10

#                 while divisor:
#                     digit = count // divisor
#                     chars[write] = chr(ord("0") + digit)
#                     write += 1
#                     count %= divisor
#                     divisor //= 10

#         return write
