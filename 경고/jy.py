input1 = input()
input2 = input()

s1 = list(map(int, input1.split(":")))
s2 = list(map(int, input2.split(":")))

s1 = s1[0] * 3600 + s1[1] * 60 + s1[2]
s2 = s2[0] * 3600 + s2[1] * 60 + s2[2]

if s2 <= s1:
    s2 += 3600 * 24
result = s2 - s1

print(f"{result//3600:0>2}:{(result%3600)//60:0>2}:{result%60:0>2}")
