contacts = {}
count = 0

def add_contact():
    name = input("주소록에 추가할 이름을 입력하세요: ")

    for i in contacts:
        if i == name:
            print("이미 존재합니다.")
            return
    
    number = input("전화번호를 입력하세요: ")
    company = input("회사 정보를 입력하세요: ")
    
    contacts[count].append(name)
    contacts[count].append(number)
    contacts[count].append(company)

    print("Contact added successfully.")
    count += 1

def update_contact():
    name = input("수정할 이름을 입력하세요: ")

    for i in contacts:
        if i == name:
            number = input("수정할 전화번호를 입력하세요: ")
            company = input("수정할 회사 정보를 입력하세요: ")
            
            contacts[count][0] = name
            contacts[count][1] = number
            contacts[count][2] = company

            print("수정 완료.")
            return

    print("해당 이름이 주소록에 존재하지 않습니다.")

def delete_contact():
    name = input("삭제할 이름을 입력하세요: ")

    for i in contacts:
        if i == name:
            del contacts[name]
            print("삭제 완료.")
            return

    print("해당 이름이 주소록에 존재하지 않습니다.")

def search_contact():
    name = input("삭제할 이름을 입력하세요: ")
    for i in contacts:
        if i == name:
            print("이름: ", contacts[count][0], "전화번호: ", contacts[count][1], "회사: ", contacts[count][2])
            return
        
    print("존재하지 않는 이름입니다.")

def display_all_contacts():
    for i in range (count):
        print("이름: ", contacts[count][0], "전화번호: ", contacts[count][1], "회사: ", contacts[count][2])

while True:
    print("주소록")
    print("1. 주소록 추가")
    print("2. 주소록 업데이트")
    print("3. 주소록 정보 제거")
    print("4. 주소록 정보 찾기")
    print("5. 주소록 모두 출력")
    print("6. 종료")
    choice = input("실행할 명령 번호를 입력하세요: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        break
    else:
        print("오류: 유효하지 않은 번호입니다.")