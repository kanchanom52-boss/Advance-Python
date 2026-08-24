def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, capacity):
        if i == 0 or capacity == 0:
            return 0
        if (i, capacity) in memo:
            return memo[(i, capacity)]
        if weights[i - 1] > capacity:
            result = solve(i - 1, capacity)
        else:
            take = values[i - 1] + solve(
                i - 1, capacity - weights[i - 1]
            )
            skip = solve(i - 1, capacity)
            result = max(take, skip)
        memo[(i, capacity)] = result
        return result

    return solve(n, capacity)


# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
answer = knapsack_top_down(weights, values, capacity)
print("Maximum value:", answer)
