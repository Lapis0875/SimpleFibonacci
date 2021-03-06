"""
피보나치 수열 코드
@author 영훈고등학교 20103 김민준 (Github 이름 : Lapis0875)
"""
from time import time
from typing import List, Callable

"""
[ 수열의 귀납적 정의 ]
수열을 처음 몇개의 항과 이웃하는 여러 항 사이의 관계식으로 정의하는 것을 수열의 귀납적 정의라고 한다.
나는 이 수열의 귀납적 정의를 활용해, 피보나치 수열을 귀납적으로 정의한 후 이를 코드로 구현하였다.
우선, 피보나치 수열을 귀납적으로 정의해보면,
```tex
a_1 = 1, a_2=1
a_n = a_(n-1) + a_(n-2) (n = 3 이상의 자연수)
```
로 나타낼 수 있다. 이러한 정의를 활용해 우리는 피보나치 수열을 정의할 것이다.
"""


# 1. 재귀호출 사용
def recursive_fibonacci(n: int) -> int:
    """
    재귀호출 방식으로 피보나치 수열의 n번째 항을 탐색합니다.
    :param n: 구하고자 하는 피보나치 수열의 항 번호입니다.
    :return: 피보나치 수열의 n 번째 항의 값을 반환합니다.
    """
    if type(n) != int or n < 1:
        raise ValueError("수열의 항 번호는 자연수여야 합니다!")

    # [ 귀납적 정의 ] a_1 = 1, a_2 = 1
    # 재귀함수 종결조건 : n=1 일 떄, 1. n=0일때, 0 (첫항부터 성립시키기 위함)
    if n == 1 or n == 2:
        return 1

    # [ 귀납적 정의 ] a_n = a_(n-1) + a_(n-2) (n = 3 이상의 자연수)
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


recursive_fibonacci.__qualname__ = "재귀함수 방식"

# 2. 동적계획법 사용
fibonacci_cache: List[int] = []


def dynamic_fibonacci(n: int) -> int:
    """
    동적 계획법 방식으로 피보나치 수열의 n번째 항을 탐색합니다.
    :param n: 구하고자 하는 피보나치 수열의 항 번호입니다.
    :return: 피보나치 수열의 n 번째 항의 값을 반환합니다.
    """
    global fibonacci_cache
    if type(n) != int or n < 1:
        raise ValueError("수열의 항 번호는 자연수여야 합니다!")

    # 캐시의 용량이 부족할 경우
    if len(fibonacci_cache) < n:
        # 캐시의 길이를 증가시킨다.
        # 초기값을 -1로 사용하는 이유는, 피보나치 수열은 음수 항을 가지지 않기 때문이다.
        fibonacci_cache.extend([-1 for _ in range(n-len(fibonacci_cache))])

    # [ 귀납적 정의 ] a_1 = 1, a_2 = 1
    # 재귀함수 종결조건 : n=1 일 떄, 1. n=0일때, 0 (첫항부터 성립시키기 위함)
    if n == 1 or n == 2:
        return 1

    # 캐시에 이미 피보나치 수열의 값이 저장되어 있을 경우, 그 값을 바로 이용한다.
    # 프로그래밍을 공부하지 않은 사람들을 위한 추가정보 :
    # 프로그래밍 언어에서, 길이 n의 리스트의 인덱스는 0부터 시작해서 n-1로 끝난다.
    # 구하고자 하는 항이 5번째 항이라면, 캐시 역할을 하는 리스트에서는 4번 인덱스의 값에 대응한다.
    if fibonacci_cache[n-1] != -1:
        return fibonacci_cache[n-1]

    # [ 귀납적 정의 ] a_n = a_(n-1) + a_(n-2) (n = 3 이상의 자연수)
    # 캐시에 피보나치 수열의 값이 존재하지 않을 경우, 최초의 1회에 안해 연산을 수행한다.
    fibonacci_cache[n-1] = dynamic_fibonacci(n - 1) + dynamic_fibonacci(n - 2)
    return fibonacci_cache[n-1]


dynamic_fibonacci.__qualname__ = "동적 계획법 방식"


# 계산 수행용 함수
def task(fibonacci_solver: Callable[[int], int], n: int) -> float:
    """
    주어진 solver를 사용해 피보나치 수열의 n번째 항을 계산합니다.
    :param fibonacci_solver: 피보나치 수열을 해결하기 위한 알고리즘을 가진 Callable한 객체입니다.
    :param n: 구하고자 하는 피보나치 수열의 항 번호입니다.
    :return: 피보나치 수열의 n번째 항을 계산하는데에 소요된 시간을 반환합니다.
    """
    task_name: str = fibonacci_solver.__qualname__ if fibonacci_solver.__qualname__ is not None else "UNKNOWN TASK"
    start = time()
    result = fibonacci_solver(n)
    print(f"[{task_name}] 피보나치 수열의 {n}번째 항 : {result}")
    end = time()
    duration = end - start
    print(f"[{task_name}] 소요시간 : {duration}초")
    return duration


def main():
    # 탐색할 피보나치 수열의 항 번호 입력받기
    n = input("탐색할 피보나치 수열의 항 번호를 입력해 주세요 > ")
    if not n.isdigit():
        raise ValueError("수열의 항 번호는 숫자여야 합니다.")
    n = int(n)
    if n < 1:
        raise ValueError("수열의 항 번호는 자연수여야 합니다.")

    # 동적 계획법 방식과 재귀함수 방식의 속도 비교
    print("[task] 동적 계획법 방식의 피보나치 수열 풀이")
    duration_dynamic = task(fibonacci_solver=dynamic_fibonacci, n=n)
    print("[task] 재귀함수 방식의 피보나치 수열 풀이")
    duration_recursive = task(fibonacci_solver=recursive_fibonacci, n=n)

    if duration_dynamic < duration_recursive:
        print("[방식비교] 동적 계획법 방식이 더 빨랐습니다!")
    elif duration_dynamic > duration_recursive:
        print("[방식비교] 재귀함수 방식이 더 빨랐습니다!")
    else:
        print("[방식비교] 두 방식 모두 동등한 결과를 보여주었습니다!")


main()
