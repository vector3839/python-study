import time
name = input("请输入要测试者的姓名：")
print("正在测试中...")
for i in range(1,101):
    print(f"{'█' * i}{i}%", end="\r")
    time.sleep(0.02)
print("\n测试完成！")
time.sleep(1)
print(f"测试结果：{name}是个SB！")