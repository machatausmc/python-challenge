import os
import csv

csvpath = os.path.join('..', 'Resources','budget_data.csv')

csvHeaderList = ["Date", "Profit/Losses", "Change"]

monthList = []
balanceList = []
averageList = []

month_count = 0
endProfit = 0
totalChanges = 0
averageChange = 0
maxDate = ""
minDate = ""
maxProfit = 0
minProfit = 0

with open (csvpath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_HeaderRow = next(csvreader)
    for row in csvreader:
        monthList.append(row[0])
        balanceList.append(row[1])
        endProfit = endProfit + int(row[1])
        change = int(balanceList[int(len(balanceList))-1]) -int(balanceList[int(len(balanceList)) - 2])
        averageList.append(change)
        totalChanges = totalChanges + change
        if change > maxProfit:
            maxProfit = change
            maxDate = row[0]
        if change < minProfit:
            minProfit = change
            minDate = row[0]

month_count = len(monthList)
averageChange = totalChanges / (len(averageList) - 1)
print("Financial Analysis")
print("-----------------------------------")
print("Number of Months: {}".format(month_count))
print("Total: ${}".format(endProfit))
print("Average Change: ${}".format(averageChange))
print("Greatest Increase in Profit : {} (${})".format(maxDate, maxProfit))
print("Greatest Decrease in Profit : {} (${})".format(minDate, minProfit))

#output file
output_txt_file = os.path.join("PyBank.txt")

#Summary Open
with open(output_txt_file, "w") as textfile:
    textfile.writelines("Financial Analysis \n")
    textfile.writelines("----------------------------------- \n")
    textfile.writelines("Number of Months: {} \n".format(month_count))
    textfile.writelines("Total: ${} \n".format(endProfit))
    textfile.writelines("Average Change: ${} \n".format(averageChange))
    textfile.writelines("Greatest Increase in Profit : {} (${}) \n".format(maxDate, maxProfit))
    textfile.writelines("Greatest Decrease in Profit : {} (${}) \n".format(minDate, minProfit))

roster = zip(monthList, balanceList, averageList)

#output csv file save
output_csv_file = os.path.join("PyBank.csv")

#open output csv file
with open(output_csv_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(csvHeaderList)

    writer.writerows(roster)

for title in roster:
    print(title)
