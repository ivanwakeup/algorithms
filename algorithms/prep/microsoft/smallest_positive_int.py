def solution(A):
    A.sort(reverse=True)
    print(A)
    for i in range(len(A) - 2, -1, -1):
        if A[i] < 0:
            continue
        chk = A[i + 1] + 1
        if A[i] > chk:
            return chk

    return A[0] + 1 if A[0] > 0 else 1


print(
    solution([1, 3, 6, 4, 1, 2])
)