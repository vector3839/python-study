score = int(input("请输入成绩："))
name = "NPC"
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