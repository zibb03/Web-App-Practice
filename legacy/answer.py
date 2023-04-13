contacts = []
count = 0

def add_contact(contacts, count):
    name = input("주소록에 추가할 이름을 입력하세요: ")

    for i in range(count):
        if contacts[i][0] == name:
            print("이미 존재합니다.\n")
            return contacts, count
    
    number = input("전화번호를 입력하세요: ")
    if len(number) == 12:
        print("올바르지 않은 번호입니다.\n")
        return contacts, count
    
    company = input("회사 정보를 입력하세요: ")
    
    contacts.append([])
    contacts[count].append(name)
    contacts[count].append(number)
    contacts[count].append(company)

    print("연락처가 추가되었습니다.\n")
    count += 1

    return contacts, count

def update_contact(contacts, count):
    name = input("수정할 이름을 입력하세요: ")

    for contact in contacts:
        if contact[0] == name:
            number = input("수정할 전화번호를 입력하세요: ")
            if len(number) == 12:
                print("올바르지 않은 번호입니다.\n")
                return contacts, count
            
            company = input("수정할 회사 정보를 입력하세요: ")
            
            contact[0] = name
            contact[1] = number
            contact[2] = company

            print("수정 완료.\n")
            return contacts, count

    print("해당 이름이 주소록에 존재하지 않습니다.\n")

    return contacts, count

def delete_contact(contacts, count):
    name = input("삭제할 이름을 입력하세요: ")

    for i in range (count):
        if contacts[i][0] == name:
            del contacts[i]
            print("삭제 완료.\n")
            count -= 1
            return contacts, count

    print("해당 이름이 주소록에 존재하지 않습니다.\n")

    return contacts, count

def search_contact(contacts, count):
    name = input("탐색할 이름을 입력하세요: ")
    for contact in contacts:
        if contact[0] == name:
            print("이름:", contact[0], "전화번호:", contact[1], "회사:", contact[2], "\n")
            return 
    
    print("존재하지 않는 이름입니다.\n")


def display_all_contacts(contacts, count):
    for i in range (count):
        print("이름:", contacts[i][0], "전화번호:", contacts[i][1], "회사:", contacts[i][2])
        if i == (count - 1):
            print()


while True:
    print("주소록")
    print("1. 주소록 추가")
    print("2. 주소록 업데이트")
    print("3. 주소록 정보 제거")
    print("4. 주소록 정보 찾기")
    print("5. 주소록 모두 출력")
    print("6. 종료\n")
    choice = input("실행할 명령 번호를 입력하세요: ")
    if choice == "1":
        contacts, count = add_contact(contacts, count)
    elif choice == "2":
        contacts, count = update_contact(contacts, count)
    elif choice == "3":
        contacts, count = delete_contact(contacts, count)
    elif choice == "4":
        search_contact(contacts, count)
    elif choice == "5":
        display_all_contacts(contacts, count)
    elif choice == "6":
        print("주소록이 종료됩니다.")
        break
    else:
        print("오류: 유효하지 않은 번호입니다.")