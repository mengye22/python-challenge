# script for poll

import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    votes = []
    Khan = []
    Correy = []
    Li = []
    Tooley = []
    for row in csvreader:
        votes.append(row[0])
        if row[2] == "Khan":
            Khan.append(row[2])
        elif row[2] == "Correy":
            Correy.append(row[2])
        elif row[2] == "Li":
            Li.append(row[2])
        else:
            Tooley.append(row[2])
            
total_votes = len(votes)
Khan_percent = round((len(Khan)/total_votes),5)
Correy_percent = round((len(Correy)/total_votes),5)
li_percent = round((len(Li)/total_votes), 5)
Tooley_percent = round((len(Tooley)/total_votes),5)
winner = max(len(Khan),len(Correy),len(Li),len(Tooley))

if winner == len(Khan):
    winner_name = "Khan"
elif winner == len(Correy):
    winner_name = "Correy"
elif winner == len(Li):
    winner_name = "Li"
else:
    winner_name = "O'Tooley"

print("Elextion Results")
print("-------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")
print("Khan: "+"{:.3%}".format(Khan_percent) + "({})".format(str(len(Khan))))
print("Correy: "+"{:.3%}".format(Correy_percent) + "({})".format(str(len(Correy))) )
print("Li: "+"{:.3%}".format(li_percent) + "({})".format(str(len(Li))))
print("O'Tooley: "+"{:.3%}".format(Tooley_percent) + "({})".format(str(len(Tooley))))
print("-------------------------------")
print(f"Winner: {winner_name}")

poll_text = open("poll.txt", "w") 
poll_text.write("Elextion Results \n")
poll_text.write("------------------------------- \n")
poll_text.write(f"Total Votes: {total_votes} \n")
poll_text.write("------------------------------- \n")
poll_text.write("Khan: "+"{:.3%}".format(Khan_percent) + "({})".format(str(len(Khan))) + "\n")
poll_text.write("Correy: "+"{:.3%}".format(Correy_percent) + "({})".format(str(len(Correy))) + "\n")
poll_text.write("Li: "+"{:.3%}".format(li_percent) + "({})".format(str(len(Li))) + "\n")
poll_text.write("O'Tooley: "+"{:.3%}".format(Tooley_percent) + "({})".format(str(len(Tooley)))+ "\n")
poll_text.write("------------------------------- \n")
poll_text.write(f"Winner: {winner_name} \n")
poll_text.close()

