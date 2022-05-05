# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election.analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print the header row
    headers = next(file_reader)
    print(headers)
    
# Close the file.

# Create a filename variable to a direct or indirect path to the file


# USing the with statement open the file as a text file






# Write 3 counties to the file (\n for next line)
  
# Close the file
