def printEntries(dict):
    for key in dict:
        print(f"{key}:{dict[key]}")

def printDicts(message, oldCol, newDict):
    print(message)
    print(f"Old collection: {oldCol}")
    print(f"New Dictionary: {newDict}")
    print("\n")

# Create a new dictionary using an existing list
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student:random.randint(1,100) for student in names}
printDicts("New dictionary from list", names, students_scores)

# Create a new dictionary using an existing dictionary and a condition
passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
printDicts("New dictionary using condition", students_scores, passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
printDicts("New dictionary listing the words in a sentence and how many letters there are in each word", sentence, result)


# Use a function to calculate new values in a dictionary
def convert_to_f(temp_c):
  return round((temp_c * (9/5)) + 32, 1)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:convert_to_f(temp) for (day, temp) in weather_c.items()}
printDicts("Convert weather report in C to F", weather_c, weather_f)

# Creating a dataFrame from a dictionary and processing that data into a new dictionary
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
high_scores = {row.student:row.score for (index, row) in student_data_frame.iterrows() if row.score > 70}
printDicts("Using pandas data frames to produce a new dict", student_dict, high_scores)

# for (index, row) in student_data_frame.iterrows():
#     print(row.student)

