import os
import csv

total_months = 0
total_net = 0
total_change = 0
average_change = 0
greatest_increase = 0
increase_date = "Jan-00"
greatest_decrease = 0
decrease_date = "Jan-00"
previous_amount = 0
current_amount = 0

income_csv = "budget_data.csv"

with open(income_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    for record in csvreader:

        if previous_amount == 0:

            total_months += 1
            total_net += float(record[1])
            previous_amount = float(record[1])

        else:

            total_months += 1
            total_net += float(record[1])

            current_amount = float(record[1])

            current_change = current_amount - previous_amount

            total_change += current_change

            if current_change > 0:

                if current_change > greatest_increase:

                    greatest_increase = current_change

                    increase_date = record[0]

            else:

                if current_change < greatest_decrease:

                    greatest_decrease = current_change

                    decrease_date = record[0]

            previous_amount = current_amount            



average_change = round(total_change/(total_months -1),2)

print("Financial Analysis")

print("-" * 20,'\n')

print("Total months = " + str(total_months),'\n')

if total_net > 0:
    print("Total Net Profit: $" + str(total_net),'\n')

else:
    print("Total Net Loss: $" + str(total_net),'\n')

print("Average Change: $" + str(average_change),'\n')

print("Greatest Increase in Profits: " + increase_date + " $" + str(greatest_increase),'\n')

print("Greatest Decrease in Profits: " + decrease_date + " $" + str(greatest_decrease))

output_file = ("budget_output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Total Months", "Total Profit", "Total Change", "Average Change", "Greatest Increase", "Date", "Greatest Decrease", "Date"])

    writer.writerow([total_months,total_net,total_change,average_change,greatest_increase,increase_date,greatest_decrease,decrease_date])
