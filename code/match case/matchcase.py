print('match ... case\n')

cmd = str.lower(input("깃 명령어 입력: "))

# The match statement evaluates the variable's value
match cmd:
    case "add":
        print("스테이지 영역에 추가")
    case "commit":
        print("깃 저장소에서 버전 관리")
    case "status":
        print("현 상황 조회")
    case "log":
        print("커밋 이력 조회")
    case _:  # the underscore character is used as a catch-all.
        print("다시 입력: ")