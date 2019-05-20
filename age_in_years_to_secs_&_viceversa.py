def  age_p():
    #prompt to ask for year / secs
    quiz=input("would you prefer your age in seconds or years (use (s)for seconds and (y)for years) ?: ")
    if quiz == ("s"):
        Value= int(input("please enter your age you've lived in seconds: "))
        print("you have lived for {} years".format(int(Value) / 60 / 60 / 24 / 365))
    elif quiz == ("y"):
        Value= int(input("please enter age your in years: "))
        print("you have lived for {} seconds".format(int(Value) * 60 * 60 * 24 * 365))
    else:
        print("ERROR!!")        
age_p()