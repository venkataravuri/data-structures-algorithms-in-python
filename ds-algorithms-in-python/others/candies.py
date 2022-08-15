def optimalCandies(n, arr):
    # every one will get one candy
    candies = [1]*n

    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candies[i+1] = candies[i]+1
    print(candies)
    for i in reversed(range(n)):
        if arr[i-1] > arr[i] and candies[i-1] <= candies[i]:
            candies[i-1] = candies[i]+1
    print(candies)
    return sum(candies)


# n = int(input())
# arr = [int(input()) for _ in range(n)]
n = 6
arr = [4, 6, 4, 5, 6, 2]
print(optimalCandies(n, arr))
