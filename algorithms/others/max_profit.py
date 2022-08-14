#https://www.techiedelight.com/find-maximum-profit-that-can-be-earned-by-selling-stocks/

def findMaxProfit(x, y, n):

    if n < 0:
        return 0

    profit = 0

    profit = max(profit, x[n] + findMaxProfit(x, y, n - 1))

    profit = max(profit, y[n] + findMaxProfit(x, y, n - 2))

    return profit


if __name__ == '__main__':
 
    x = [5, 3, 4, 6, 3]
    y = [8, 4, 3, 5, 10]
 
    print('The maximum profit earned is', findMaxProfit(x, y, len(x) - 1))