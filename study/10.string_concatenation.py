str1 = "hello"
str2 = "world"
print(str1 + " " + str2)
print("good " * 3)

print("he" in str1)
print("elo" not in str1)

print(str1[0])
print(str1[-1])

print(str1[:3]) # 从0开始，包含0，不包含3
print(str1[1:4]) # 从1开始，包含1，不包含4
print(str1[-3:-1]) # 从-3开始，包含-3，不包含-1
print(str1[-1::-1])