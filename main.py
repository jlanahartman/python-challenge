
"""

# loop through the csv file to find: 
    
    -The total number of months included in the dataset

    -The net total amount of "Profit/Losses" over the entire period

    -The changes in "Profit/Losses" over the entire period, and then the average of those changes

    -The greatest increase in profits (date and amount) over the entire period

    -The greatest decrease in profits (date and amount) over the entire period
"""

import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, "r") as csvFile:
    csvRead = csv.reader(csvFile, delimiter=",")

    next(csvRead)


    # Delcare variables 
    count_months = 0
    total_revenue = 0
    monthly_change = 0
    previous_month = 0
    total_monthly_change = []
    max_change = 0
    min_change = 0
    max_date = ""
    min_date = ""


    for row in csvRead:
        count_months = count_months + 1
     # print(count_months)
        PL = int(row[1])
        total_revenue = total_revenue + PL 
        # previous_month = PL
        if count_months > 1:
            monthly_change = PL - previous_month
            total_monthly_change.append(monthly_change)
        if monthly_change > max_change:
            max_change = monthly_change
            pl_date=row[0]
            max_date = pl_date
        if monthly_change < min_change: 
            min_change = monthly_change
            pl_date=row[0]
            min_date = pl_date

            previous_month = PL

      #   avg_profit_loss = sum(monthly_change/len(total_monthly_change))
      #   avg_profit_loss = round(avg_profit_loss, 2)

        # print(avg_profit_loss)
        print(max_date)



    # Print statemnets

    print(f"Financial Analysis") 

    print("-----------------------")

    print(f"Total Months: {count_months}")

    print(f"Total: {total_revenue}")

    print(f"Average Change: {total_monthly_change}")

    print(f"Greatest increase in profits: {max_date}")

    print(f"Greatest increase in profits: {min_date}")

















































        



       