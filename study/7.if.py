score = int(input("请输入成绩："))
name = "NPC"

# if语句是Python中用于条件判断的语句，可以根据不同的条件执行不同的代码块。基本的if语句结构如下：
if score == 100:
    print("你真棒！", end = "")
    if name == "NPC":
        print("但你是NPC！")
elif 80 <= score < 100:
    print("你很棒！")
elif 60 <= score < 80:
    print("你还行！")
elif 0 <= score < 60:
    print("你需要努力了！")
else:
    print("分数无效！")