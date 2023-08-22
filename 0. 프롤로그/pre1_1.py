M = 10
N = 100


def check(remain, pre):
    # 배치할 사람이 더 이상 없으면 종료
    if remain < 0:
        return 0
    elif remain == 0:
        return 1
    cnt = 0
    for i in range(pre, M + 1):  # 테이블에 배치할 사람 수만큼 반복
        cnt += check(remain - i, i)
    return cnt


print(check(N, 2))
