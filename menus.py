def add_student():
        with open("student_log.txt", "a") as file:

            while True:
                name = input("Enter Student Name OR 3 to exit:")

                if name.lower() == "3":
                    break

                file.write(name + "\n")
        
        print("All students saved successfully.")  
    


def view_student():
        with open("student_log.txt", "r") as file:
            print("\nStudent List:")
    
            for student in file:
                print(student.strip())
                
print("1. Add Student")
print("2. View Student")
print("3. Exit")

option = input("Choose Option : 1 OR 2 OR 3 :")

if option == "1":
    add_student()

elif option == "2":
    view_student()

elif option == "3":
    print("Thank You !")
else:
    print("Invalid Option") 