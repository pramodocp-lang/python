with open("student_log.txt", "a") as file:

    while True:
        name = input("Enter Student Name (or 'exit' to stop): ")

        if name.lower() == "exit":
            break

        file.write(name + "\n")

print("All students saved successfully.")


with open("student_log.txt", "r") as file:
    print("\nStudent List:")
    
    for student in file:
        print(student.strip())