# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("===================================")
print("    Stock Portfolio Tracker")
print("===================================")

number_of_stocks = int(input("How many different stocks do you have? "))

for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Investment for", stock_name, "=", investment)

    else:
        print("Stock not available in the price list.")

print("\n===================================")
print("Total Investment Value =", total_investment)
print("===================================")

# Save result into a text file
file = open("portfolio_result.txt", "w")

file.write("Stock Portfolio Result\n")
file.write("----------------------------\n")
file.write("Total Investment Value: $" + str(total_investment))

file.close()

print("\nResult has also been saved in portfolio_result.txt")
