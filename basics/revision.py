def guess_favourite(fruits):
    guess = int(input("Enter your guess (1-5):"))
    print()
    if guess == 1:
        print("You are wrong!")
        print()
        guess_favourite(fruits)
    elif guess ==2:
        print("Very Close")
        print()
        guess_favourite(fruits)
    elif guess == 3:
        print("That's not correct!")
        print()
        guess_favourite(fruits)
    elif guess ==4:
        print(f"Yes! It's {fruits[4]}")
        print()
    else:
        print("Try Again!")
        print()
        guess_favourite(fruits)
        




fruits = ["Banana", "Mango", "Apple", "Orange","Grapes"]

print("\n List of my favourite food lists")
print();

print(fruits);
print();
guess_favourite(fruits)
    


    
