import random
i=0
a= random.randint(1,10)
while i<2:
    a= random.randint(1,10)
    my= input("홀 짝? (잘못 입력하면 한번은 기회 줄게)")
    print(my)
    if my != "홀" and my != "짝": 
        
        i=i+1
        print("잘못 입력 다시 입력해라 ")
        

    else:    
        dab = ""
        if a % 2 == 0:
            print("짝")
            dab = "짝"
        else:
            print("홀")
            dab = "홀"

        if my == dab :
             print("맞다 ")


        else:
             print("빵") 
if i==2:
    print("빵")    
    print("게임종료")   

   












