"""
피보나치 수열 코드
"""
from time import time
from typing import List, Callable


# 1. 재귀함수 이용
def recursive_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("수열의 항 번호는 음수가 될 수 없습니다!")

    # 종결조건 : n=1 일 떄, 1. n=0일때, 0 (첫항부터 성립시키기 위함)
    if n <= 1 :
        return n

    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# 2. 동적계획법 사용
fibonacci_cache: List[int] = []


def dynamic_fibonacci(n: int) -> int:
    global fibonacci_cache
    if n < 0:
        raise ValueError("수열의 항 번호는 음수가 될 수 없습니다!")

    # cache is blank (initial state)
    if len(fibonacci_cache) == 0:
        # initialize cache
        fibonacci_cache = [0 for i in range(n+1)]

    # 종결조건 : n=1 일 떄, 1. n=0일때, 0 (첫항부터 성립시키기 위함)
    if n <= 1:
        fibonacci_cache[n] = n
        return n

    # 캐시에 이미 피보나치 수열의 값이 존재할경우, 그 값을 바로 이용한다.
    if fibonacci_cache[n] != 0:
        return fibonacci_cache[n]
    # 캐시에 피보나치 수열의 값이 존재하지 않을 경우, 최초의 1회에 안해 연산을 수행한다.
    fibonacci_cache[n] = dynamic_fibonacci(n - 1) + dynamic_fibonacci(n - 2)
    return fibonacci_cache[n]


def task(fibonacci_solver: Callable[[int], int], n: int):
    """
    Solve fibonacci problem with given solver.
    :param fibonacci_solver: Callable instance which has algorithm to solve fibonacci problem.
    :param n: target index of fibonacci sqeuence
    :return: target
    """
    print("피보나치 수열의 ㅖ{")
    start = time()
    result = fibonacci_solver(n)
    print(result)
    end = time()
    print(f"{end - start}초 경과")


print("동적 계획법 방식의 피보나치 수열 풀이")
task(fibonacci_solver=dynamic_fibonacci, n=40)
print("재귀함수 방식의 피보나치 수열 풀이")
task(fibonacci_solver=recursive_fibonacci, n=40)
