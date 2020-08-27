def calMinCoins(coins,amount):

    coins = sorted(coins,reverse =True) #O(nlogn)

    if amount<coins[-1]:
        return -1
    count=0
    i=0
    while amount: #O(n)            time complexity O(nlogn) + O(n) = O(nlogn)

        num = amount//coins[i]
        amount-=num*coins[i]

        count+=num

        if num:
            print(f'coin {coins[i]} : {num}')

        i+=1

coins = [2000,500,100,50,20,10,5,2,1]

calMinCoins(coins,283)






