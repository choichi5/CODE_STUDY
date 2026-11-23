from collections import deque

def solutions(N, K):
    queue = deque(range(1,N+1))

    while len(queue) > 1:
        for _ in range(K-1):
            queue.append(queue.popleft())

            queue.popleft()
    return queue[0]

print(solutions(5,2))
    