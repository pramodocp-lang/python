def square(n):
    return n*n;

def table(n):
    counter = 1
    while counter<=10:
        print("\n")
        print(n*counter)
        counter +=1



def print_options():

        print("\n")
        print()
        print("1. Square")
        print("2. Table")
        print("3. Show User")


print("This is function revision")

print_options();

while True:
    number = int(input("Enter the to squar:"))
    sq = square(number)
    print(sq)
    option = input("Continue: Y/N")
    if option in("Y","y"):
        continue
    else:
        break
        
print("Print the Table: Enter the number")
 
while True:
    number = int(input("Enter the to number:"))
    table(number)
    option = input("Continue: Y/N")
    if option in("Y","y"):
        continue
    else:
        break
 
user_profile = [
    {
        "Name": "Pramod",
        "Age": 23
    },
    {
        "Name": "Sanjay",
        "Age": 34
    }
]

print(user_profile[0]["Name"])
       
       
 
 
 
 
 