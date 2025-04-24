def alpha(word):
    word = word.upper()
    cnt = {}

    for ch in word:
        if ch in cnt:
            cnt[ch] += 1
        else:
            cnt[ch] = 1
    max_cnt = max(cnt.values())
    most = [i for i, j in cnt.items() if j == max_cnt]

    if len(most) > 1:
        return "?"
    else:
        return most[0]


n = input()
print(alpha(n))
