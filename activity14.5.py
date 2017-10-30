import numpy

myDictionary = {}
print "Please enter the list of student names and corresponding GPAs."
studentName = raw_input("Student Name [X to exit]: ")
if studentName != "X":
    studentGPA = input("Student GPA: ")
while studentName != "X":
    myDictionary[studentName] = studentGPA
    studentName = raw_input("Student Name [X to exit]: ")
    if studentName != "X":
        studentGPA = input("Student GPA: ")

#Loop through entries and display names and GPAs
highest = 0.0
lowest = 4.0
print "Class GPA List"
for key,value in myDictionary.items():
    print key, ":", value
    if value > highest:
        highest = value
    if value < lowest:
        lowest = value

#Get Average
gpas = myDictionary.values()
totalGPA = 0

for gpa in gpas:
    totalGPA = totalGPA + gpa

#output analysis
print "Average GPA: ", (totalGPA/len(gpas))
print "Highest GPA: ", highest
print "Lowest GPA: ", lowest
print "Median GPA: ", numpy.median(gpas)



