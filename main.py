# This is the main python file that will be used to pull in the information/code from all other files in my Stuent Feedback Project


from dictionaries.student_names import student_names
#print(student_names) #added the print to seach section so I could test as I was going along.

from dictionaries.performance_categories import performance_categories
#print(performance_categories)

from dictionaries.score_descriptions import score_descriptions
#print(score_desciptions)


print("Welcome to the Student Feedback Report\n")
input("Press Enter to continue...")
print("As the Tutor you will be marking your students on the following\n")


for category in performance_categories:
    print(f"-{category}")
    
input("Press Enter to continue...")
    
print("Using the follwoing scoring key, you need to mark each category 1 - 4 for each student\n")




for key, values in score_descriptions.items():
    print(f"{key} = {values}")
    
    
input("Press Enter to continue...")







