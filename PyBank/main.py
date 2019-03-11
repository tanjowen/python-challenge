

import os 
import csv


csvpath = os.path.join("Resources", "budget_data.csv")

preset = 0
difference = 0
max_ = 0
min_ = 0
month_count = 0
total = 0
monthly_change = []

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header =next(csvreader)
	
	for money in csvreader:
		month = money[0]
		monthly_bal = int(money[1])
		difference = monthly_bal - preset
		if difference > max_:
			max_ = difference
			max_date = month
		if difference < min_:
			min_ = difference
			min_date = month
		preset = monthly_bal
		month_count = month_count + 1
		total = total + monthly_bal
		monthly_change.append(difference)

	average = (sum(monthly_change)-monthly_change[1])/ (len(monthly_change)-1)




print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${total}')
print(f'Average Change: ${round(average, 2)}')
print(f'Greatest Increase in Profits: {max_date} (${max_})')
print(f'Greatest Decrease in Profits: {min_date} (${min_})')

output_path = os.path.join("Financial Analysis.csv")

with open(output_path, "w", newline="") as csvfile:
	new = csv.writer(csvfile, delimiter=',')

	new.writerow(['Financial Anlysis'])
	new.writerow(['----------------------------'])
	new.writerow([f'Total Months: {month_count}'])
	new.writerow([f'Total: ${total}'])
	new.writerow([f'Average Change: ${round(average, 2)}'])
	new.writerow([f'Greatest Increase in Profits: {max_date} (${max_})'])
	new.writerow([f'Greatest Decrease in Profits: {min_date} (${min_})'])

