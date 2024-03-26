def square_root(n):
    if n < 2:
        return n

    left, right = 1, n // 2
    while left <= right:
        mid = (left + right) // 2
        squared = mid * mid
        if squared == n:
            return mid
        elif squared < n:
            left = mid + 1
        else:
            right = mid - 1

    return right
