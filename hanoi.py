def f(bar1 : int, bar2 : int, n : int):
    if n == 1:
        print(bar1, '번째 기둥에 있는', n, '번째 원반을', bar2,'번째 기둥으로 옮기셈')
        return
    A = 6 - bar1 - bar2
    f(bar1, A, n - 1)
    print(bar1, '번째 기둥에 있는', n, '번째 원반을', bar2,'번째 기둥으로 옮기셈')
    f(A, bar2, n - 1)
n = int(input('원판 수 입력하쇼 : '))
print('최소 "', (n ** 2) - 1, '"트 만에 가능')
print('원판이 20개 이하일때만 상새 과정 출력할거임')
if not n > 20:
    print(f'ㅇㅋ {n}개 이니 상새 과정 출력함')
    f(1, 3, n)
    print('이제 님은 개임을 클리어함')