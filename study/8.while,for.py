import time
#while ture:就是一直循环，直到break
# i = 1
# while i <= 100:
#     print(f"{i}%", end = "\r")
#     i += 1
#     time.sleep(0.01)
# print("")

# for循环是Python中一种常用的循环结构，用于遍历可迭代对象（如列表、字符串、字典等）中的元素。for循环的基本语法如下：
# for 变量 in 可迭代对象:
for i in range(1, 99):
    print(f"{i}%", end = "\r")
    time.sleep(0.01)
print("99%", end = "\r")
time.sleep(0.5)
print("100%")
time.sleep(0.5)

str = "Hello, World!"
# for循环可以用来遍历字符串中的每个字符，使用变量i来表示当前遍历到的字符。
for i in str:
    print(i, end = "|")
print("")

for i in range(1, 6):
    print(i, end = " ")
print("")

for i in range(1, 10, 2):
    print(i, end = " ")
print("")

# 以下是一个使用for循环计算1到100的和的示例：
add = 0
for i in range(1, 101):
    add += i
print(f"1到100的和是: {add}")

# continue语句用于跳过当前循环中的剩余代码，并继续下一次循环。break语句用于终止整个循环。
for i in range(1,5):
    if i == 3:
        continue
    print(i, end = " ")
print("")

for i in range(1, 5):
    if i == 3:
        break
    print(i, end = " ")