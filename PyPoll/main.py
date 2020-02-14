#import dependenceies
import os 
import csv

#Setting paths
    #path to read csv
csvpath=os.path.join('Resources','election_data.csv')
print(csvpath)
    #path for  output file
outputPath=os.path.join("Resources", "ElectionData")

#initialize variables
candidates=[]
voteCounts=[]
numOfVotes=0



#iterate through the dataset line by line

for line in csvreader:
    #count of total number of votes in dataset
    numOfVotes= numOfVotes+1
    #candidate votes
    candidate=line[2]

    #If candidate has votes than add to vote counts for each candidate type
    if candidate in candidates:
        candidate_Index=candidates.index(candidate)
        voteCounts[candidate_Index]=voteCounts[candidate_Index]+1
    # If the candidate is not already in the array, then add to list
    else:
        candidates.append(candidate)
        voteCounts.append(1)
percentages=[]
max_votes=voteCounts[0]
max_index=0

#find the winner of the election
for count in range(len(candidates)):
    voteInPercentage=(voteCounts[count]/numOfVotes)*100
    percentages.append(voteInPercentage)
    if voteCounts[count]>max_votes:
        max_votes=voteCounts[count]
        print(max_votes)
        max_index=count
winner=candidates[max_index]



#print final results

print("Election Results")
print("------------------------------")
print(f"Total Votes:{numOfVotes}")

for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({voteCounts[count]})")
print("------------------------------")

print(f"Winner:{winner}")
print("------------------------------")

write_file=f"PyPoll_results_summary.txt"

#open write_file
filewriter= open(write_file, mode="w")

#print final results in a text file

filewriter.write("Election Results\n")
filewriter.write("------------------------------\n")
filewriter.write(f"Total Votes:{numOfVotes}\n")
filewriter.write("------------------------------\n")

for count in range(len(candidates)):
    filewriter.write("------------------------------\n")
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({voteCounts[count]})\n")
    filewriter.write("------------------------------\n")
    filewriter.write(f"Winner:{winner}\n")
    filewriter.write("------------------------------\n")

#close the file once data is entered in txt file
filewriter.close()







with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    #Then skip the header
    line=next(csvreader,None)

    for line in csvreader:
        totalMonths=totalMonths+1
        rowAmt=float(line[1])
        currentRowAmt=float(rowAmt)

        totalSum=totalSum+rowAmt
        if(previousRowAmt!=0):
            change=rowAmt-previousRowAmt
        
        previousRowAmt=currentRowAmt
        
        currentchange=change+previousChange
        
        previousChange=currentchange
        
        change_list.update({line[0]:change})   

        
    print("Financial Analysis")
    print("----------------------------") 
    print("Total Months:",totalMonths)
    print("Total: $",totalSum)
    print("Total change: $",currentchange/(totalMonths-1))
    print("Greatest Increase in Profits:",max(zip(change_list.values(), change_list.keys())))
    print("Greatest Decrease in Profits:",min(zip(change_list.values(), change_list.keys()))) 
