file = open("student_log.txt", "a")

student_name = input("Enter Studdent Name   :")

file.write(student_name + "\n")

print("Student Saved Successfully!")
file.close()

file = open("student_log.txt", "r");

print(file.read());

file.close();

