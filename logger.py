import csv
import os

filename = "data.csv"

class batch :
    def __init__(self, ticker, action, price, amount):
        ticker = self.ticker
        action = self.action
        price = self.price
        amount = self.amount


def append_to_csv(ticker, accs_bought, accs_sold, net):
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header only if file doesn't exist
        if not file_exists:
            writer.writerow(["DATE", "TICKER", "#accs bought", "#accs sold", "NET"])
        
        # Append the new row
        writer.writerow([date, ticker, accs_bought, accs_sold, net])

#Use rolling counter 
# def generate_batch(ticker, action, price): 

# Example usage
# append_to_csv("10/12/2024", "FGF", 50, 49, 1200)