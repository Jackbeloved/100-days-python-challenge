# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
print(student_scores['Harry'])

student_grades ={}
for i in student_scores:
    print(i)
    if student_scores[i] <70:
        result = "fail"
    elif 71< student_scores[i] <80:
        result = "Acceptable"
    elif 81 < student_scores[i] < 90:
        result = "Exceeds Expectations"
    else:
        result = "Outstanding"
    student_grades[i]= result

print(student_grades)




