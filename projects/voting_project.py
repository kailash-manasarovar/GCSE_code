no_of_candidates = 4
candidate_names = ["A", "B", "C", "D"]
votes = {}
for i in range(0, no_of_candidates):
    votes[candidate_names[i]] = 0
print(votes)
## user votes for C
votes["C"] += 1
print(votes)
## another use votes for C
votes["C"] += 1
print(votes)






# ## create a 2d array of the correct size
# no_of_cands = 4
# candidate_names = ["A", "B", "C", "D"]
# vote_counts = []
# for i in range(0, no_of_cands):
#     vote_counts.append([candidate_names[i]])
# print(vote_counts)
# ## add votes
# ## user inputs A = 1 vote
# vote_counts[0].append(1)
# print(vote_counts)
# ## next user inputs A = 1 vote
# vote_counts[0][1] += 1
# print(vote_counts)





