# 문제
# 문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 줄의 수 N이 주어진다.
# 다음 N개의 줄에는 문장이 주어진다.
# 각 문장에 들어있는 글자의 수는 30을 넘지 않는다.
# 모든 줄의 첫 번째 글자는 알파벳이다.

# 출력
# 각 줄의 첫글자를 대문자로 바꾼뒤 출력한다.

import sys

tc = int(sys.stdin.readline())
for t in range(tc):
    sntnce = sys.stdin.readline().rstrip()
    for i in range(len(sntnce)):
        if i == 0:
            print(sntnce[i].upper(), end="")
        else:
            print(sntnce[i], end="")
    print("")