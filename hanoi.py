from typing import List, Callable

# 스택을 리스트로 정의
Stack = List[int]

# 스택 초기화 함수
def init_stack() -> Stack:
    return []

# 스택이 비었는지 확인하는 함수
def is_empty(stack: Stack) -> bool:
    return len(stack) == 0

# 스택에 데이터를 추가하는 함수
def push(stack: Stack, data: int) -> Stack:
    return [data] + stack

# 스택에서 데이터를 제거하고 반환하는 함수
def pop(stack: Stack) -> (int, Stack):
    if is_empty(stack):
        raise ValueError("Stack underflow")
    return stack[0], stack[1:]

# 디스크를 한 막대에서 다른 막대로 이동하는 함수
def move_disk(src: Stack, dest: Stack, s: str, d: str) -> (Stack, Stack):
    if is_empty(src):
        raise ValueError("Cannot move from an empty stack")
    disk, src = pop(src)
    dest = push(dest, disk)
    print(f"Move disk {disk} from {s} to {d}")
    return src, dest

# 하노이 탑 문제를 재귀적으로 해결하는 함수
def hanoi(n: int, src: Stack, aux: Stack, dest: Stack, s: str, a: str, d: str) -> (Stack, Stack, Stack):
    if n == 0:
        return src, aux, dest
    if n == 1:
        src, dest = move_disk(src, dest, s, d)
    else:
        src, aux, dest = hanoi(n - 1, src, dest, aux, s, d, a)
        src, dest = move_disk(src, dest, s, d)
        aux, src, dest = hanoi(n - 1, aux, src, dest, a, s, d)
    return src, aux, dest

# 메인 함수
def main():
    n = 3  # 원판의 수를 3으로 고정

    # 세 개의 스택 초기화
    src = init_stack()
    aux = init_stack()
    dest = init_stack()

    # 초기 상태에서 src 스택에 디스크 추가
    for i in range(n, 0, -1):
        src = push(src, i)

    # 하노이 탑 문제 해결
    src, aux, dest = hanoi(n, src, aux, dest, 'A', 'B', 'C')

if __name__ == "__main__":
    main()
