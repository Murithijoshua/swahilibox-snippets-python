#function that allows user to guess a number stored within the program i.e magic number
def magic():
    play=input("guess any number between 0-10?:  ")
    number=int(play)
    if number == 8:
        play=int(number)
        print("you've won!!")
    else:
        print("too bad try nex time!!")
magic()

        