class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        input: array of numbers
        output: profit which is integer
        rules:
        1. Each number in the array represents a price.
        2. Choose a day to buy a coin and then a different day to sell.
        3. Maxium profit you can achieve. 
        4. You can choose not to make a transaction so its 0

        [10,1,5,6,7,1]
                    x   

        [10,8,7,5,2]
                  x

        buy = 2
        profits = 0

        minimize our buy. min(buy, current_price)
        If the current price is greater than our buy price.
        curr_profits = current_price - buy
        profits = max(profits, curr_profits)



        Algo:
        1. initialize buy to infinity and profits to 0
        2. We minimize the buy price by doing min(buy, current_price)
        3. If current_price > buy price:
            profits = max(current_price - buy, profits)
        4. return profits
        '''
        buy = float("inf")
        profits = 0

        for price in prices:
            buy = min(price, buy)
            if price > buy:
                profits = max(price - buy, profits)

        return profits
