import random
print("오징어 게임에 참가하셨습니다.")
print("이번 게임은 다리 건너기 입니다")

print("오른쪽 왼쪽 중에 선택 하세요")

print("1번은 왼쪽 2번은 오른쪽")

for i in range(10):
    dap= random.randint(1,2)
    print(dap)
    where=int(input("선택하세요(숫자만):1번은 왼쪽 2번은 오른쪽"))
    print(dap)
#내가 선택에 따라 살고 죽는다
    if where== 1:
        
        dr="왼쪽"
    else: 
        
        dr="오른쪽"

    if where ==dap :
        print("{}번으로 점프".format(i+1))
        print("{}으로 점프".format(dr))
        print("{}칸 남았습니다".format(9-i))
    else:
        print("{}으로 점프".format(dr))
        print("으아아아악~")
        break 

if i==9:
    print("클리어")

