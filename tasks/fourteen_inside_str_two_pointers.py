def is_subsequence(s1, s2):
    i, j = 0, 0  # i для s1, j для s2
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)  # Если прошли по всей s1, значит s1 является подпоследовательностью s2