str = "hello world"
# 字符串的操作，打印子串
print("he" in str, "elo" not in str)
print(str[0], str[-1])
print(str[:3], str[1:4], str[-3:-1], str[-1::-1])

# find和count方法，find方法可以指定起始位置和结束位置，count方法也可以指定起始位置和结束位置
print(str.find("or", 4,9), str.count("o", 4, 8))
# index 没找到会报错，find 没找到会返回-1

# replace方法，replace方法可以指定替换的次数
print(str.replace("o", "0", 1)) # 替换第一个o为0, replace默认替换全部
print(str.replace(str[7], "0"))

# split方法，split方法可以指定分隔符和分割次数
print(str.split("o")) # 默认以空格分割

str1 = "hello World"
# capitalize方法：将字符串的第一个字符转换为大写字母，其他字符转换为小写字母；
# upper方法：将字符串中的所有字符转换为大写字母；
# lower方法：将字符串中的所有字符转换为小写字母；
# title方法：将字符串中的每个单词的首字母转换为大写字母，其他字符转换为小写字母
print(str1.capitalize(), str1.upper(), str1.lower(), str1.title())

# startswith方法：判断字符串是否以指定的子字符串开头；可以指定起始位置和结束位置
# endswith方法：判断字符串是否以指定的子字符串结尾，可以指定起始位置和结束位置
print(str.startswith("he", 0, 2), str.endswith("ld", 9, 11))

# isalpha判断字符串是否全为字母，isdigit判断字符串是否全为数字，
# isspace判断字符串是否全为空格，islower判断字符串是否全为小写字母，isupper判断字符串是否全为大写字母
print(str.isalpha(), str.isdigit(), str.isspace(), str.islower(), str.isupper()) 

print(str.ljust(20, "*")) # 在字符串右边添加*，使总长度为20

print(str.rjust(20, "*")) # 在字符串左边添加*，使总长度为20

print(str.center(20, "*")) # 在字符串两边添加*，使总长度为20

print(str.strip("hd"), str.lstrip("hd"), str.rstrip("hd")) # 去掉字符串两端的h和d, lstrip去掉左边的，rstrip去掉右边的