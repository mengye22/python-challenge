# script for budget_data.csv
import os
import csv

print("Financial Analysis")
print("-------------------------------")

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_month = []
    pro_los = []
    change = []

    for row in csvreader:
        total_month.append(row[0])
        pro_los.append(int(row[1]))

    for i in range(len(pro_los)-1):
        change.append(pro_los[i+1] - pro_los[i])

sum_month = len(total_month)
profit_losses = sum(pro_los)
profit_change = round(sum(change) / len(change),2)
greatest_inc = max(change)
greatest_dec = min(change)
greatest_inc_month = change.index(max(change)) + 1
greatest_dec_month = change.index(min(change)) + 1

print(f"Total MonthS: {sum_month}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${profit_change}")
print(f"Greatest Increase in Profits: {total_month[greatest_inc_month]} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {total_month[greatest_dec_month]} (${greatest_dec})")


bank_text = open("bank.txt", "w") 
bank_text.write("Financial Analysis \n")
bank_text.write("---------------------------- \n")
bank_text.write(f"Total MonthS: {sum_month} \n")
bank_text.write(f"Total: ${profit_losses} \n")
bank_text.write(f"Average Change: ${profit_change} \n")
bank_text.write(f"Greatest Increase in Profits: {total_month[greatest_inc_month]} (${greatest_inc}) \n")
bank_text.write(f"Greatest Decrease in Profits: {total_month[greatest_dec_month]} (${greatest_dec}) \n")
bank_text.close()

    

