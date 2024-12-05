from typing import List, Callable

Stack = List[int]

def init_stack() -> Stack:
    return []

def is_empty(stack: Stack) -> bool:
    return len(stack) == 0

def push(stack: Stack, data: int) -> Stack:
    return [data] + stack

def pop(stack: Stack) -> (int, Stack):
    if is_empty(stack):
        raise ValueError("Stack underflow")
    return stack[0], stack[1:]

def move_disk(src: Stack, dest: Stack, s: str, d: str) -> (Stack, Stack):
    if not is_empty(src):
        disk, new_src = pop(src)
        new_dest = push(dest, disk)
        print(f"Move disk {disk} from {s} to {d}")
        return new_src, new_dest
    return src, dest

def hanoi(n: int, src: Stack, aux: Stack, dest: Stack, s: str, a: str, d: str) -> (Stack, Stack, Stack):
    if n == 0:
        return src, aux, dest
    
    if n == 1:
        new_src, new_dest = move_disk(src, dest, s, d)
        return new_src, aux, new_dest
        
    src, aux, dest = hanoi(n - 1, src, dest, aux, s, d, a)
    src, dest = move_disk(src, dest, s, d)
    aux, src, dest = hanoi(n - 1, aux, src, dest, a, s, d)
    return src, aux, dest

def main():
    n = 3
    src = init_stack()
    aux = init_stack()
    dest = init_stack()
    
    for i in range(n, 0, -1):
        src = push(src, i)
    
    src, aux, dest = hanoi(n, src, aux, dest, 'A', 'B', 'C')

if __name__ == "__main__":
    main()