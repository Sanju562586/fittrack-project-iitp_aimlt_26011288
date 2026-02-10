name = input("Enter your name: ")
n = int(input("Enter the number of games you did play: "))
total_score = int(input("Enter the total score you got: "))
average_score = total_score / n

print(f"Player: {name}")
print(f"Games played: {n}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")