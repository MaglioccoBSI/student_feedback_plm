# This is the main python file that will be used to pull in the information/code from all other files in my Stuent Feedback Project


from dictionaries.student_names import student
#print(student_names) #added the print to seach section so I could test as I was going along.

from dictionaries.performance_categories import performance_categories
#print(performance_categories)

from dictionaries.score_descriptions import score_descriptions
#print(score_desciptions)


print("Welcome to the Student Feedback Report\n")
input("Press Enter...\n")
print("As the Tutor you will be marking your students on the following\n")


for category in performance_categories:
    print(f"- {category}")
    
print() # This is a blank line for when code is run
input("Press Enter...\n")
    
print("Using the following scoring key, you need to mark each category 1 - 4 for each student\n")




for key, value in score_descriptions.items():
    print(f"{key} = {value}")
    
print() # This is a blank line for when code is run    
input("Press Enter For A List of Students...\n")

for category in student:
    print(f"- {category}")
    
print() # This is a blank line for when code is run    


student = "Peter"  # 

print(f"\nEnter scores for {student}:")

for student_name in student:
    print(f"\nEnter scores for {student_name}:")

    for category in performance_categories:
        while True:
            try:
                score = int(input(f"- {category} (1-4): "))
                if score in [1, 2, 3, 4]:
                    student[student_name][category] = score  # store the score
                    break  # exit the while loop
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

print(f"\nScores for {student} recorded successfully!")









