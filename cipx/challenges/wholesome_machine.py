def main():
    
    affirm = "I can do anything I put my mind to."

    user_input = input("Please type the following affirmation: I can do anything I put my mind to.\n")

    while user_input != affirm:
        print("That was not the affirmation.")
        user_input = input("Please type the following affirmation: I can do anything I put my mind to.\n")

    print("That's right! :)")


if __name__ == "__main__":
    main()
