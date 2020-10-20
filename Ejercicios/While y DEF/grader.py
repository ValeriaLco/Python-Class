def average(a, b, c):
    promedio_parciales = (a + b +c)/3
    return(promedio_parciales)

def numerical_final_grade (a, b, c, d, e):
    three_partials = ((a + b + c)/3) * 0.50
    final_project = e * 0.15
    final_exam = d * 0.35
    numerical = three_partials + final_project + final_exam
    return numerical

def letter_grade (a, b, c, d, e):
    calif = (((a + b + c)/3) * 0.50) + (e * 0.15) + (d * 0.35)
    if calif > 90:
        letter = 'A'
        return letter
    elif calif > 80:
        letter = 'B'
        return letter
    elif calif > 70:
        letter = 'C'
        return letter
    elif calif > 60:
        letter = 'D'
        return letter
    else:
        letter = 'F'
        return letter
    
first_partial_exam = int(input())
second_partial_exam = int(input())
third_partial_exam = int(input())
final_exam = int(input())
final_project = int(input())

if first_partial_exam < 0:
    first_partial_exam = 0
elif first_partial_exam > 100:
    first_partial_exam = 100
    
if second_partial_exam < 0:
    second_partial_exam = 0
elif second_partial_exam > 100:
    second_partial_exam = 100
    
if third_partial_exam < 0:
    third_partial_exam = 0
elif third_partial_exam > 100:
    third_partial_exam = 100
    
if final_exam < 0:
    final_exam = 0
elif final_exam > 100:
    final_exam = 100

if final_project < 0:
    final_project = 0
elif final_project > 100:
    final_roject = 100
    
a = first_partial_exam
b = second_partial_exam
c = third_partial_exam
d = final_exam
e = final_project

print(average(a, b, c))
print(numerical_final_grade(a, b, c, d, e))
print(letter_grade(a, b, c, d, e))