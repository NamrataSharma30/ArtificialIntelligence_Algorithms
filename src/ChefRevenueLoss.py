price = []
items_price_ceiling = {}
list_of_prices = []
loss = 0
temp = 0
print("Please enter the number of test cases between 1 and 100")
T = int(input())
for _ in range(T):
    print("Please enter the number of items (between 1 and 10,000) and the price ceiling (between 1 and 1000)")
    N, K = input().split(" ")
    print("Please enter the price of the items between 1 and 1000")
    price = list(input().split(" "))
    N = int(N)
    K = int(K)
    items_price_ceiling[N] = K
    for i in range(len(price)):
        price[i] = int(price[i])
    list_of_prices.append(price)

for number_of_test_case in range(T):
    key_number = list(items_price_ceiling.keys())[number_of_test_case]
    if temp < number_of_test_case:
        loss = 0
    for i in range(key_number):
        temp = number_of_test_case
        value = list(items_price_ceiling.values())[number_of_test_case]
        if list_of_prices[number_of_test_case][i] > value:
            loss = loss + (list_of_prices[number_of_test_case][i] - value)
    print("Loss for test case", number_of_test_case + 1, "is", loss)
