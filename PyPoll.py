# Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initalize a total vote counter
total_votes = 0 

# Candidate Options
candidate_options = []
# declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker 
winning_candidate = "" 
winning_count = 0 
winning_percentage = 0 

# Open election results and read the file
with open(file_to_load) as election_data:
   
# To Do: Perform Analysis
    # Open Election Results and read file
    file_reader = csv.reader(election_data)

    # Read the header rows
    headers = next(file_reader)

    # Print each row in csv file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

        # Print candidate name for each row
        candidate_name = row[2]
        
        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add it to the list of candidates
            candidate_options.append(candidate_name)
            # 2 Begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0 

        # adding votes to each candidate
        candidate_votes[candidate_name] += 1 
        
    # save the results as a txt file
    with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # write total election results to text file 
        txt_file.write(election_results)
        
        # Determine the percentage of votes for each candidate by looping through counts 
       
        # 1 Iterate through the candidate list
        for candidate_name in candidate_votes:
            # 2 retrieve vote count for candidate
            votes = candidate_votes[candidate_name]
            # 3 calc percentage of votes
            vote_percentage = float(votes)/ float(total_votes) * 100

        # print(winning_candidate_summary)

            # To do: print out the winning candidate, vote count and percentage to
            # terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        
        print(winning_candidate_summary)
        # Save the final vote count to the text file.
        txt_file.write(winning_candidate_summary)

