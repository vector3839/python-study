i = 1
import time
#while ture:就是一直循环，直到break
# while i <= 100:
#     print(f"\r{i}%", end = "")
#     i += 1
#     time.sleep(0.01)
# print("")

for i in range(1, 99):
    print(f"\r{i}%", end = "")
    time.sleep(0.01)
print("\r99%", end = "")
time.sleep(0.5)
print("\r100%")
time.sleep(0.5)

str = "Hello, World!"
for i1 in str:
    print(i1, end = "|")
print("")

for i2 in range(1, 6):
    print(i2, end = " ")
print("")

for i3 in range(1, 10, 2):
    print(i3, end = " ")
print("")

add = 0
for i4 in range(1, 101):
    add += i4
print(f"1到100的和是: {add}")

for i5 in range(1,5):
    if i5 == 3:
        continue
    print(i5, end = " ")
print("")

for i6 in range(1, 5):
    if i6 == 3:
        break
    print(i6, end = " ")