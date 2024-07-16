def main():
    print("Welcome to the adventure game!")
    print("You find yourself in a dark forest.")
    choice = input("Would you like to go left or right? ")

    if choice.lower() == "left":
        print("You encounter a bear and it attacks you. Game Over!")
    elif choice.lower() == "right":
        print("You find a path leading out of the forest.")
        choice = input("Would you like to follow the path or go back? ")

        if choice.lower() == "follow":
            print("You follow the path and find a treasure chest!")
            print("Congratulations, you won the game!")
        elif choice.lower() == "back":
            print("You go back into the forest and get lost. Game Over!")
        else:
            print("Invalid choice. Game Over!")
    else:
        print("Invalid choice. Game Over!")

if __name__ == "__main__":
    main()
