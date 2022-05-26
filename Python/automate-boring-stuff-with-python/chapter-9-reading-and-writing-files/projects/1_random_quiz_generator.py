# Generating Random Quiz Files, Automate the boring stuff with python, page number: 221

import shelve
from random import shuffle, sample


quiz_dir = r"learning-programming\Python\automate-boring-stuff-with-python\chapter-9-reading-and-writing-files\projects\quiz-data"

# quiz data
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# generate 35 quiz files
for quiz_num in range(35):
    # create quiz and answer key files
    with open(f"{quiz_dir}\\capital_quiz_{quiz_num + 1}", "w") as quiz_file:

        # write header for the quiz
        quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
        quiz_file.write((" " * 20) + f"State Capitals Quiz (Form{quiz_num + 1})")
        quiz_file.write("\n\n")

        # shuffle the order of the states
        states = list(capitals.keys())
        shuffle(states)

        for question_num, state in enumerate(states):
            correct_answer = capitals[state]
            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            
            wrong_answers = sample(wrong_answers, 3)
            answer_options = wrong_answers + [correct_answer]
            shuffle(answer_options)
            
            # Write the question and the answer options to the quiz file.
            quiz_file.write(f"{question_num + 1}. What is the capital of {state}?\n")
            for i in range(4):
                quiz_file.write(f" {'ABCD'[i]}. { answer_options[i]}\n")
                quiz_file.write('\n')
            

            with open(f"{quiz_dir}\\capital_quiz_answers_{quiz_num + 1}", "a") as answer_file:
                answer_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
