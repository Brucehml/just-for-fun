def is_palindrome(s):
    return s == s[::-1]

# 示例代码
s1 = "abcba"
s2 = "hello"
print(is_palindrome(s1)) # True
print(is_palindrome(s2)) # False
