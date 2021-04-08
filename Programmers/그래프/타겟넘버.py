answer = 0


def dfs(idx, sum_, numbers, target):
    total = sum(numbers)
    n = len(numbers)
    global answer

    if idx == n:
        if 2 * sum_ - total == target:
            answer += 1
    else:
        dfs(idx + 1, sum_ + numbers[idx], numbers, target)
        dfs(idx + 1, sum_, numbers, target)

    return answer