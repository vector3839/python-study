st = "你好，世界！"

# 将字符串编码为字节串
st1 = st.encode("utf-8")
print(st1)
# 将字节串解码为字符串
st2 = st1.decode("utf-8")
print(st2)