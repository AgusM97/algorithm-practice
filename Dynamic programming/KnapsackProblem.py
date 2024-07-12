print("Weights:")
weights = [int(n) for n in input().split(" ")]
print("Values:")
values = [int(n) for n in input().split(" ")]
print("Max weight:")
maxWeight = int(input())
maxValue = 0
dp = [[0 for n in range(maxWeight + 1)] for n in values]
for i in range(len(values)):
    for j in range(maxWeight + 1):
        if j == 0:
            dp[i][j] = 0
        elif weights[i] > j:
            dp[i][j] = dp[i][j - 1]
        elif weights[i] <= j:
            if i == 0:
                dp[i][j] = values[i]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
        maxValue = max(maxValue, dp[i][j])
print(f"Max Value: {maxValue}")
