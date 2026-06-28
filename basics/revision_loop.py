fruits = ["Banana", "Mango", "Apple", "Orange","Grapes"]
print();

def show_menu(fruits):
    print();
    print("\nList of my favourite food lists\n")
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")

show_menu(fruits)    



attempts  = 0;
while True:
      
      print()

      try:
        guess = int(input("Enter your guess (1-5): "))
        attempts  = attempts  + 1  
      except ValueError:
        print("❌ Please enter numbers only.")
        continue
      if guess ==1:
            print("Wrong")
            print()
      elif guess in(2, 3):
            print("Very Close")
            print()
      elif guess == 4:
            print("Congratulations!")
            print()
            print(f"You guessed correctly in {attempts} attempts.")
            play = input("Do you want to play again? (y/n)")
            if play in("Y","y"):
                show_menu(fruits)
                attempts = 0
                continue
            break
      elif guess ==5 :
            print("Not Correct!")
            print()
      else:
            print("Please enter a number between 1 and 5.")
            
         

    
