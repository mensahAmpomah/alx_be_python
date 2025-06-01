size = int(input("Enter the size of the pattern: "))
star = True

while star:
       if star:
            for i in range(size):
                #    print("", end="\n")
                for j in range(size):
                        print("*", end="")

                print()    
            star = False
       else:
             break     



