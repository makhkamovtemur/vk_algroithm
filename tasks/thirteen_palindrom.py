def is_palindrome_stack(s):
    cleaned = "".join([c.lower() for c in s if c.isalnum()])
    stack = []
    for char in cleaned:
        stack.append(char)

    # палиндром с использованием стека
    for char in cleaned:
        if stack.pop() != char:
            return False
    return True

def is_palindrome_two_pointers(s):
    cleaned = "".join([c.lower() for c in s if c.isalnum()])
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True