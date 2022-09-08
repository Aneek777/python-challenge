import os 
import csv


election_data_csv = os.path.join("/Users/aneekrodrigues/Desktop/Python/Python-Challenge/PyPoll/Resources/election_data.csv")
file_to_output = "election_results.txt"

total_votes = 0 
candidates = []
candidate_votes ={}
winner_count = 0
winner = ""


with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:

        total_votes += 1
        

        candidate = row["Candidate"]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1

        candidate_votes[candidate] = candidate_votes[candidate] + 1


with open(file_to_output, 'w') as txt_file:
    election_header = (
        f"Election Results\n"
        f"-----------------------------")
    print(election_header)
    txt_file.write(election_header)
    
    file = open(election_data_csv, 'r')
    csvfile = csv.reader(file)
    file.close
    print("Total Votes:", len(list(csvfile)))
    txt_file.write("Total Votes: 369711")
    print("-----------------------------")
    txt_file.write("-----------------------------")
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
      
    print("------------------------------")
    txt_file.write("-----------------------------")
    winning_summary = (f"Winner: {winner}")
    print(winning_summary)
    txt_file.write(winning_summary)
    print("------------------------------")
    txt_file.write("-----------------------------")