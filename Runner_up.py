n = int(input())  # Read the number of scores
scores = list(map(int, input().split()))  # Read the scores as a list

unique= list(set(scores))  # Remove duplicates by converting to a set
unique.sort(reverse=True)  # Sort in descending order

runner_up = unique_scores[1]  # Second highest score
print(runner_up)
