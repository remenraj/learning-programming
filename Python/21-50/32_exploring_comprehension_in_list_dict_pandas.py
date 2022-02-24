#############################
##### List Comprehension ####
#############################

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)


# name = "Angela"
# letter_list = [char for char in name]
# print(letter_list)


# # creating a list of numbers
# number_list = [num * 2 for num in range(1, 5)]
# print(number_list)


# # adding a condition
# new_num_list = [num for num in number_list if num == 2]
# print(new_num_list)


# # capitalize words in a list having more than 4 letters
# names = ["james", "john", "jack", "jill", "jennifer", "jones"]
# capitalized_names = [name.upper() for name in names if len(name) > 4]
# print(capitalized_names)


###########################
##### Dict comprehension ##
###########################

# import random
# names = ["james", "john", "jack", "jill", "jennifer", "jones"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {
#     student:score for (student, score) in student_scores.items() if score > 60
# }
# print(passed_students)


# # converting a sentence into a list of words and adding it into a dictionary with its length as values
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)


# # converting weather dictionary of temperature in celsius to temperature in fahrenheit
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {
#   day:(temp * (9 / 5) + 32) for (day, temp) in weather_c.items()
# }
# print(weather_f)


########################
######## pandas ########
########################

# import random, pandas

# student_dict = {
#     "student": ["james", "john", "jack", "jill", "jennifer", "jones"],
#     "score": [random.randint(1, 100) for _ in range(6)],
# }
# # looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key, value)

# student_df = pandas.DataFrame(student_dict)
# # looping through dataframe
# # for (key, value) in student_df.items():
# #     print(key, value)

# for (index, row) in student_df.iterrows():
#     print(row.student, row.score)
#     if row.student == "jack":
#         print("Jack scored", row.score)
