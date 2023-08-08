# import poll
import os
import csv

# open and read csv
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
  # Create the lists  
    votes = []
    county = []
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []
  # Initialize the variables as required.
    Charles_Casper_Stockham_votes = 0
    Diana_DeGette_votes = 0
    Raymon_Anthony_Doane_votes = 0

    # read each row of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # VOTE COUNT
    total_votes = (len(votes))
   

    # Votes per person
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidates)
            Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
        elif candidate == "Diana DeGette":
            Diana_DeGette.append(candidates)
            Diana_DeGette_votes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(candidates)
            Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
    
   
    
    
    # Percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
    Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)
    

    
    # Winner 
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        winner = "Charles_Casper_Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
        winner = "Diana_DeGette"  
    else:
        winner = "Raymon_Anthony_Doane"


     #  Print the analysis to the terminal 
    print(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')


    #  Export a text file with the results

    file = open("Results.txt","w")
    file.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''') 
    file.close()
    