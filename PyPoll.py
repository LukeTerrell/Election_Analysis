# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis','election_analysis.txt')

# Initialize total voter count
total_votes = 0
# Create a new list for Candidate options
candidate_options = []
# Create an empty dictionary fill with candidates and their votes
candidate_votes = {}
# Declare a variable for the winning candidate
winning_candidate = ""
# Declare cariable for the winning count equal to 0
winning_count = 0
# Declare a variable for the winning_percentage equal to 0
winning_percentage = 0

# Open Election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze data here.
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Skip the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
    
    # Print Candidate name from each row
        candidate_name = row[2]

    # If candidate name does not match existing candidate
        if candidate_name not in candidate_options:

            #add it to the list of options
            candidate_options.append(candidate_name)

            # Track Candidates vote count
            candidate_votes[candidate_name] = 0

        # Add vote to that candidate's count
        candidate_votes[candidate_name] += 1
    # Save the results to text file
    with open(file_to_save, 'w') as txt_file:
        # Print final vote count to the terminal
        election_results = (
            f'\nElection Results\n'
            f'-------------------------\n'
            f'Total Votes: {total_votes:,}\n'
            f'-------------------------\n')
        print(election_results, end='')
        # Save the final vote count to the text file
        txt_file.write(election_results)
        # Iterate through candidate options
        for candidate_name in candidate_votes:

            # Retrieve vote counts for each candidate
            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes
            vote_percentage = (float(votes) / float(total_votes)) * 100

            #Print out each candidate's name, vote count, and percent total votes
            candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
            print(candidate_results)
            # Save the candidate results to out text file.
            txt_file.write(candidate_results)
            # Determine if the vote count that was calculated is greater than winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If the vote count is that was calculated is greater then the winning count and percentage is greater than winning percentage, set winningcount eqaul to votes and percent
                winning_count = votes
                winning_percentage = vote_percentage
                # Set winning count equal to variable, candidatename in the for loop
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f'-------------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'-------------------------\n'
        )
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)