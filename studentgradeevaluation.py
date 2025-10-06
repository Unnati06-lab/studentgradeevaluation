# Initialize an empty list to store marks
mark = []

# Loop to get marks from the user
for i in range(5):
    marke = float(input(f"Enter marks for member {i+1}: "))
    mark.append(marke)

# Calculate the average
average = sum(mark) / len(mark)

# Display the result
print(f"\nThe average marks of the 5 members is: {average:.2f}")