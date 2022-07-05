# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
i = 0
student_heights_sum = 0
for height in student_heights:
    i += 1
    student_heights_sum += height

student_heights_average = int(round(student_heights_sum / i, 0))
print(student_heights_average)
