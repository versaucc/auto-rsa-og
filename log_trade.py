
import csv
import os
import datetime as d 

# Can be manipulated


def append_to_csv(action, symbol, price):
    filename = "trade_log.csv"
    # file_exists = os.path.isfile(filename)
    
    print('Logging Trade')
    # date = d.datetime.now().strftime("%m/%d/%Y")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        print('loggging again')
        # Write header only if file doesn't exist
        # if not file_exists:
        writer.writerow(["ACTION", "TICKER", "PRICE"])
        
        # Append the new row
        writer.writerow([action, symbol, price])



# Test
append_to_csv("SELL", "FGF", 5.01)