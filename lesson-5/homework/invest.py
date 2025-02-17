def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount += (amount * rate)
        print(f"year {1}: {amount:.2f}") 

amount = int(input("Enter the initial amount of the money: "))
rate = float(input("Enter the rate of change: "))
years = int(input("Enter the number of years: "))

invest(amount, rate, years)