import random


print("오늘 점심 뭐 먹지")
#메뉴 리스트 
menu=["짜장면","짬뽕","라면","김밥","돈까스",]
for i in menu:
    print(i)

print("이 중에서 제가 추천하는 메뉴는:{}".format(menu[random.randint(0,4)]))