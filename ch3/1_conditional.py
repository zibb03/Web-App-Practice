# 자연수를 분류하는 문제

# 분류할 수를 저장한 변수 num 
num = -11

if num > 0:
    print("양수 입니다.")

    # 중첩 if 조건문
    if num > 100:
        print("이 수는 100보다 큽니다.")
elif num == 0: 
    print ("0 입니다.")
else:
    # 위의 조건문에 모두 해당하지 않을 경우
    print ("음수 입니다.")