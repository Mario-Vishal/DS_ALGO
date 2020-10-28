'''
Coin Change Problem - how many ways you can form the change from the given coins
'''

#Approach 1 -- naive approach

def rec_coin(target,coins):

    #default value set to target
    min_coins = target

    #base case to see if target is in coins
    if target in coins:
        return 1
    else:
        # for every coin value i.e <= target
        for i in [c for c in coins if c<=target]:

            #add a coin count + recursive 
            num_coins = 1 + rec_coin(target-i,coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


#Approach 2 - Dynammic Programming


def rec_coin_dynamic(target,coins,known_results):

    #default value set to target
    min_coins = target

    #base case to see if target is in coins
    if target in coins:
        known_results[target] = 1
        return 1

    #return a known result if it happens to be greater than 1
    elif known_results[target]>0:
        return known_results[target]

    else:
        # for every coin value i.e <= target
        for i in [c for c in coins if c<=target]:

            #add a coin count + recursive 
            num_coins = 1 + rec_coin_dynamic(target-i,coins,known_results)

            if num_coins < min_coins:
                min_coins = num_coins

                #reset that known result
                known_results[target] = min_coins

    return min_coins

target = 15
coins = [1,5,10,12]  
know_results = [0]*(target+1)
print(rec_coin_dynamic(target,coins,know_results))