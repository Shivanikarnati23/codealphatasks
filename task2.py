stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}  
print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not found. Choose from available list.")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity
total_value = 0

print("\nPortfolio Summary:")
print("------------------------")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(stock, "| Quantity:", qty, "| Price:", price, "| Value:", value)

print("------------------------")
print("Total Investment Value:", total_value)
save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    file_type = input("Save as .txt or .csv? ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("------------------------\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock} - Quantity: {qty}, Price: {stock_prices[stock]}, Value: {stock_prices[stock]*qty}\n")
            file.write(f"\nTotal Investment: {total_value}")
        print("Saved as portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
            file.write(f"Total,,, {total_value}")
        print("Saved as portfolio.csv")

    else:
        print("Invalid file type.")

print("\nProgram Finished!")
