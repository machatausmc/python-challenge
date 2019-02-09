import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

reader = csv.reader(csvpath, delimiter = ",")
data = list(reader)
row_count = len(data)
print("Number of votes: " + row_count)