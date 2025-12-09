# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])

# ----------------------------------------
for fruit in fruits: # this is a lot shorter --> "for loop" 
    print(fruit)
# i just worked with loops

# ----------------------------------------
# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)

# ----------------------------------------
# print out each subject but stop when you reach "History"
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    if subject == "History":
        break
    print(subject)

# ----------------------------------------
# skip over "Science and print the rest:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    if subject == "Science":
        break
    continue
    print(subject)

# ----------------------------------------
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for index in range(len(subjects)):
    print("Subject " + str(index) + ": "+ subjects[index])

# Given:
numbers = [5, 10, 15, 20]

# ----------------------------------------
# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0
for number in numbers: 
    total += number
    print("total: " ,total)

# first time = 0
# second time total = 0 + 5
# third time total = 5 + 10
# fourth time total = 15 + 15
# fifth time total = 30 + 20

# ----------------------------------------
new_numbers = list(range(1, 600001))
# this creates a list of numbers from 1 to 600000
# Challenge: sum up all the numbers from 1 to 600000
total = 0
for new_number in new_numbers: 
    total += new_number
print("total: " ,total)

# ----------------------------------------
next_numbers = list(range(5,26))
total = 0
for next_number in next_numbers:
    total += next_number
print("total: " ,total)