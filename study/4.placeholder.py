name = "Alice"
age = 30
print("my name is %s and I am %d years old" % (name, age))

a = 123
print("%6d,%06d" % (a, a)) # %6d表示输出的整数占6个字符宽度，右对齐，%06d表示输出的整数占6个字符宽度，右对齐，前面补0

b = 3.1415926
print("%f" % b) # %f表示输出的浮点数默认保留6位小数,遵循四舍五入原则
print("%.2f" % b) # %.2f表示输出的浮点数保留两位小数
print("%8.2f" % b) # %8.2f表示输出的浮点数占8个字符宽度，右对齐，保留两位小数

print("%%" % ()) # 输出%符号，%%表示输出一个%符号

print(f"My name is {name} and I am {age} years old") # f-string格式化字符串，使用{}括起来的变量会被替换成对应的值