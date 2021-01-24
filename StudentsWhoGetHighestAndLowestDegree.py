students=[]
grades=[]
while(1):
    student=input("Enter the name:")
    if student=="end":
        break
    else:
        students.append(student)
        grades.append(int(input("what is the grades of {}:".format(student))))
def LowestGrade(students,grades):
    lowestGrade=100
    indexes=[]
    for grade in grades:
        if grade<lowestGrade:
            lowestGrade=grade
    i=0
    for grade in grades:
        if lowestGrade==grade:
            indexes.append(i)
        i+=1
    print("Students that gets the lowest grade:")
    for index in indexes:
        print(students[index])    
def HighestGrade(students,grades):
    highestGrade=0
    indexes=[]
    for grade in grades:
        if grade>highestGrade:
            highestGrade=grade
    i=0
    for grade in grades:
        if highestGrade==grade:
            indexes.append(i)
        i+=1
    print("Students that gets the higheast grade:")
    for index in indexes:
        print(students[index])
        
        
LowestGrade(students, grades)
HighestGrade(students, grades)