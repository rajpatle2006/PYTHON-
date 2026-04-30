s = "programming"
ch = 'm'

result = []

for i in range(len(s)):
    if s[i] == ch:
        result.append(i)

print(result)