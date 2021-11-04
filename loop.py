import random
i=0
a= random.randint(1,10)
marble= 10
print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

while i<2:
    a= random.randint(1,10)
    print("당신의 구슬의 갯수: {}개".format(marble))
    bet= input("구슬 몇개 배팅? (잘못 입력하면 한번은 기회 줄게)")
    if int(bet)>marble:
        i=i+1 
        print("배팅갯수 초과 다시 입력 ")
        continue
    

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
             marble= marble+int(bet)
             print("당신의 구슬의 갯수 :{}개".format(marble))
             if marble>=20 :
                 print("이겼다 다음 스테이지")
                 break

        else:
             print("틀렸다 구슬 뺏김") 
             marble= marble-int(bet)
             print("당신의 구슬의 갯수 :{}개".format(marble))
             if marble ==0 :
                print("빵")
                print("게임종료") 
                break
if i==2:
    print("빵")    
    print("게임종료")   



   

   












