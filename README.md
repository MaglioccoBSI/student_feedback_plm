# student_feedback_plm

Activity 2.1 - Coding Fundamentals: Project Brief - Automated Student Feedback Generator

The brief has been taken from Repo: https://github.com/chris-reeves1/python29-09-25 (report/report.md) and has been 
pasted at the bottom of this readme file.

After reading the brief, I started my planning and design journey by first creating this repo (https://github.com/MaglioccoBSI/student_feedback_plm.git) and tested I could pull and push to it.

I then started to breakdown the brief by first creating the student_design.xlsx file just so I could picture
what an overall table of results would look like against each student.

The table contained the student name, the score category, the score and a key that represents the score value which will be used as the phrase  



Project Brief — Automated Student Feedback Generator

Overview
--------

You are required to design and implement a Python program that generates personalised feedback for students based on a set of scores (1–4). The program should produce a feedback file for each learner using a consistent template and mapped phrases. Instead of submitting only the code, you will evidence your design and outputs in a report. The report should include screenshots, explanations, and reflections to demonstrate functionality.

Requirements
------------

- A list of students (at least 3 for demonstration)

- For each student, input scores (1–4) for the following attributes:
    - Overall performance
    - General understanding
    - Contribution level
    - Lab completion
    - Punctuality
    - Engagement
    - Further study level

- Use score to phrase mappings (dictionary lookups) to convert numeric values into appropriate sentences.
    (Example: performance_map = {1: "basic", 2: "ok", 3: "good", 4: "excellent"})

- Apply the mappings inside a feedback template, for example:
    template = f"General Comments\n{student_name} performed {performance_map[overall]} in this module...\n\n"
    template += f"Punctuality\n{punctuality_map[punctuality]}...\n\n"
    template += f"Further Learning\n{further_study_map[further_study]}..."

- Save one feedback file per student in a folder called feedback/.

- File name format: feedback/<student_name>_feedback.txt.

- Automatically open the file in an editor for final manual edits/approval.

Additional Requirements
-----------------------

- Code quality:
    - Clear naming conventions.
    - Readable structure with comments and docstrings.
    - Modular design (functions for mapping, file writing, etc.).

- Stretch goal:
    - Format CLI outputs with colours/spaces.

Deliverables
------------

- Report (Word or PDF) containing:
    - Explanation of your design choices.
    - Screenshots of your Python code.
    - Screenshots of the program running in the terminal (showing coloured output if implemented).
    - Screenshots of the generated feedback/ directory.
    - Screenshot of one feedback file open in an editor.
    - Reflection section explaining:
        - How your mapping design supports reusability.
        - What you would improve if given more time.

    note: you can include full code in an appendix. 

You have a maximum of 3 hours to complete both the program and the report.


---------------------------------------------------------------------------------------------------------------------------------
Example completed feedback: 

General comments
Mark did well in this module. He demonstrated a good understanding of concepts we covered and showed he has a broad knowledgebase. 
He contributed to discussions and asked relevant questions. 

Learner Punctuality and engagement 
Mark was punctual throughout the module and engaged well through Webex. 

Recommendations on further learning
Continue to practice the basics of containerisation, Kubernetes and pipelines.

Marking Rubric: 

Program Functionality: 25%
Template Design & Mapping 15%
Code Quality 20%
Report Quality 20%
Reflection & Understanding 10%
Stretch CLI Formatting 10%



