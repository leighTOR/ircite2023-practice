def longest_palindrome(s):
    l = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            ss = s[i:j+1]
            if ss == ss[::-1] and len(ss) > len(l):
                l = ss
    print(l)


s = "babad"
longest_palindrome(s)
