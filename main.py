# Create List

ns = "\n"

cle = " "

win = 0
lose = 0

list = [[0]*4 for i in range(3)]
list2 = [['?']*4 for q in range(3)]

print(list)

for j in range(len(list)):
    for k in range(len(list[j])):
        ans = int(input("숫자를 입력해 주세요"))
        list[j][k] = ans


while win <= 2 or lose <= 10:

    for a in range(len(list2)):
        for b in range(len(list2[j])):
            print(f"[{a}][{b}]: {list2[a][b]}",
                  end=f"{ns if (b==3 or b==6 or b==9) else cle}")

    print("맞추실 행과 열을 입력해 주세요")

    ans1 = int(input("행 :"))
    ans2 = int(input("열 :"))

    print(f"[{ans1}][{ans2}] 열을 입력하였습니다.")
    print("정답을 입력해주세요")
    ans3 = int(input("답 :"))

    if ans3 == list[ans1][ans2]:
        list2[ans1][ans2] = ans3
        print("정답을 맞추셨습니다.")
        win += 1
    else:
        print("틀리셨습니다. 10번 틀릴시 패배합니다")
        lose += 1
