import csv
import os


months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ['',99999999999999]
total = 0

path = os.path.join("Resources", "PyBank_Resources_budget_data.csv")

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    months = months + 1
    total = total + int(first_row[1])
    previous_net = int(first_row[1])

    for row in csvreader:
        months = months + 1
        total = total + int(first_row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


monthly_average = sum(net_change_list)/len(net_change_list)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${monthly_average}")
print(f"Greatest increase in profits: {greatest_increase[0]} {greatest_increase[1]}")
print(f"Greatest decrease in profits: {greatest_decrease[0]} {greatest_decrease[1]}")    

export = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${monthly_average}\n"
    f"Greatest increase in profits: {greatest_increase[0]} {greatest_increase[1]}\n"
    f"Greatest decrease in profits: {greatest_decrease[0]} {greatest_decrease[1]}")
with open("main.txt", 'w') as txt_file:
    txt_file.write(export)