from itertools import accumulate

base_price = 100
additional_service_prices = [10, 30, 40]

print(list(accumulate(additional_service_prices, initial=base_price)))
