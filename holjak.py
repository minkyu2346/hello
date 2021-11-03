import random
print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다")

while True:
    a= random.randint(1,10)
    print(a)
    my=str(input("홀수 또는 짝수를 입력하세요 "))
    if a%2 == 0:
        print("구슬은 짝수 입니다")
        a= "짝수"
        if a == my :
            print("정답")
        else: 
            print("틀림")

    else:
        print("구슬은 홀수 입니다")
        a= "홀수"    
        if a== my : 
            print("정답")
        else: 
            print("틀림")
            

            
        