print("hi whats your name?")
name = input('>')
if name == "jack":
    print("hi master")
print("hi " + name + "!")
print("im going to try and guess")
print("your favorite ice cream flavor out of these 7")
print("stawberry, blueberry, cookie dough, vanilla bean")
print("cookies and cream, cotton candy, and chocolate!")

print("does it have berry in its name?")

berry = input(">")
while berry != "yes" and berry != "no":
    berry = input("please type yes or no:")
# berry output
if berry == "yes":
    print("is it a red berry?")

    red = input(">")
    while red != "yes" and red != "no":
        red = input("please type yes or no:")
    

    if red == "yes":
        print("is it strawberry?")
        one = input(">")
        
        while one != "yes" and one != "no":
            one = input("please type yes or no:")

        if one == "no":
            print("i give up")

        elif one == "yes":
            print("Yay!")
        

    elif red == "no":
        print("is it blueberry?")
        two = input(">")
        
        while two != "yes" and two != "no":
            one = input("please type yes or no:")

        if two == "no":
            print("i give up")

        elif two == "yes":
            print("Yay!")
        
# non berry output
elif berry == "no": 
    print("is it cookie realated?")
    
    cookie = input(">") 
    while cookie != "yes" and cookie != "no":
        cookie = input("please type yes or no:")
    
    if cookie == "yes":
        print("does it have cream in its name?")
        cream = input('>')
        while cream != "yes" and cream != "no":
            cream = input("please type yes or no:")
        
        if cream == "yes":
            print("is it cookies and cream?")
            three = input(">")
        
            while three != "yes" and three != "no":
                one = input("please type yes or no:")

            if three == "no":
                print("i give up")

            elif three == "yes":
                print("Yay!")

        elif cream == "no":
            print("is it cookie dough?")
            four = input(">")
            
            while four != "yes" and four != "no":
                four = input("please type yes or no:")

            if four == "no":
                print("i give up")

            elif four == "yes":
                print("Yay!")
            

    elif cookie == "no":
        print("does it have candy in its name?")
        
        candy = input('>')
        while candy != "yes" and candy != "no":
            candy = input("please type yes or no:")
                          
        if candy == "yes":
            print("Is it cotton candy?")

            five = input(">")
            
            while five != "yes" and five != "no":
                five = input("please type yes or no:")

            if five == "no":
                print("i give up")

            elif five == "yes":
                print("Yay!")

        elif candy == "no":
            print("does it have bean in its name?")
            bean = input('>')
            while bean != "yes" and bean != "no" and bean != "beans?":
                bean = input("please type yes or no:")
                
            if bean == "yes":
                print("is it Vanilla Bean?")
                six = input(">")
            
                while six != "yes" and six != "no":
                    six = input("please type yes or no:")

                if six == "no":
                    print("i give up")

                elif six == "yes":
                    print("Yay!")

            elif bean == "no":
                print("Is it Chocolate?")
                seven = input(">")
                
                while seven != "yes" and seven != "no":
                    seven = input("please type yes or no:")

                if seven == "no":
                    print("i give up")

                elif seven == "yes":
                    print("Yay!")

            elif bean == "beans?" and name == "bean":
                print("beans, beans, beans I love beans? is it a bean?")
                
                love = input(">")
                while love != "yes" and love != "no":
                    love = input("please type yes or no:")

                if love == "yes":
                    print("yay I love beans too!")

                elif love == "no":
                    print("does that mean we can't have beans together?")


