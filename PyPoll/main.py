# This program reads in the results from the following five counties:
# Bamoo, Marsh, Queen, Raffah and Trandee.
# Results are summarized into totals results for the election.

import csv

# Initialize the variables

candidate = "none"
total_votes = 0
total_correy = 0
total_khan = 0
total_li = 0
total_otooley = 0
correy_pct = 0
khan_pct = 0
li_pct = 0
otooley_pct = 0
max = 0
winner = "none"


# Create the lists for the election.
# The candidate portion will need to be updated for each election


candidate_list = []        # Stores the candidate names
vote_pct_list = []         # Stores the percentage of votes for candidates
vote_total_list = []       # Stores the total votes for candidates
election_dict =[]          # Dictionary which stores the election results by candidate



poll_txt = "poll_results.txt"       # File that holds all the election data


# Main program

with open(poll_txt, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    csvheader = next(csvreader)

    # Loop through the file and calculate the total votes for each candidate
    for record in csvreader:                                

        candidate = record[2]

        total_votes += 1

        if candidate == "Correy": total_correy += 1 
        if candidate == "Khan": total_khan += 1
        if candidate == "Li": total_li += 1
        if candidate == "O'Tooley": total_otooley += 1

# The following code determines who the winner is

max = total_correy
winner = "Correy"
if total_khan > max:
    max = total_khan
    winner = "Khan"
    if total_li > max:
        max = total_li
        winner = "Li"
        if total_otooley > max:
            winner = "O'Tooley"


# This code calculates the percentage for each candidate

correy_pct = round((total_correy/total_votes),2)
khan_pct = round((total_khan/total_votes),2)
li_pct = round((total_li/total_votes),2)
otooley_pct = round((total_otooley/total_votes),2)

# Creating the three lists to be used to create the dictionary of election results

candidate_list.append("Correy")
candidate_list.append("Khan")
candidate_list.append("Li")
candidate_list.append("O'Tooley")

vote_pct_list.append(correy_pct)
vote_pct_list.append(khan_pct)
vote_pct_list.append(li_pct)
vote_pct_list.append(otooley_pct)

vote_total_list.append(total_correy)
vote_total_list.append(total_khan)
vote_total_list.append(total_li)
vote_total_list.append(total_otooley)

# Creation of the dictionary of election results

election_dict = dict(zip(candidate_list, zip(vote_pct_list, vote_total_list)))

# Print out the election results

print("    Election Results")
print("-" * 25,'\n')
print("   Total Votes: " + str(total_votes))
print("-" * 25,'\n')
for k,vv in sorted(election_dict.items(), key=lambda p:p[1], reverse=True):
     print("{} : {}".format(k,vv))
print("-" * 25,'\n')
print("   Winner: " + winner)

# Save the dictionary of election results as a text file 

outputfile = open("election_dict.txt","w")
outputfile.write( str(election_dict) )
outputfile.close()