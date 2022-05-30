# random输出随机数，randint
import random

con = random.randint(1, 100)
print(con)
while con > 1:
    print("都是最棒吧")
    con = con - 1
