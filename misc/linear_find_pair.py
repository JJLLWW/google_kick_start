def find_pair(A, s):
    n = len(A)
    i, j = 0, n-1
    while A[i] + A[j] != s:
        if A[i] + A[j] < s:
            i += 1
        elif A[i] + A[j] > s:
            j -= 1
        # break
        if i == j:
            return "no"
    return A[i], A[j]

if __name__ == "__main__":
    print(find_pair([1,2,3,4], 5))
    print(find_pair([1,10,100], 66))