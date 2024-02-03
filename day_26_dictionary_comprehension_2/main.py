data = '{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}'

weather_c = eval(data)
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def convert_to_f(temp_c):
  return (temp_c * (9/5)) + 32

weather_f = {day:convert_to_f(temp) for (day, temp) in weather_c.items()}

print(weather_f)