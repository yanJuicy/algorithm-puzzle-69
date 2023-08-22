M = 10
N = 100

memo = {}


def check(remain, pre):
    # 이전에 계산한 적 있다면, 메모했던 값을 반환
    key = str([remain, pre])
    if key in memo:
        return memo[key]

    # 배치할 사람이 더 이상 없으면 종료
    if remain < 0:
        return 0
    elif remain == 0:
        return 1
    # 재귀적 처리
    cnt = 0
    for i in range(pre, M + 1):  # 테이블에 배치할 사람 수만큼 반복
        cnt += check(remain - i, i)
    # 계산 결과를 메모하면서 반환
    memo[key] = cnt
    return cnt


print(check(N, 2))
