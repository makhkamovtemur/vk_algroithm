def move_zeros_to_end(scores):
    non_zero_index = 0
    for i in range(len(scores)):
        if scores[i] != 0:
            scores[non_zero_index], scores[i] = scores[i], scores[non_zero_index]
            non_zero_index += 1
    return scores