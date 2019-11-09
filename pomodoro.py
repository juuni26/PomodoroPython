import os

choice = 1
while choice:
    print("welcome to  MySpaceTime !")
    print("1. start/Reset")
    print("2. add")
    print("3. show pomodoro now")
    print("4. Exit")
    choice = int(input("masukkan pilihan: "))

    if choice==1:
        os.system('CLS')
        print("starting ......")
        print("pomodoro now resetting to 0")
        f=open("list.txt","w")
        f.write("0")
        f.close()
        print("\n\n\n")
        
       
    elif choice==2:
        os.system('CLS')
        
        f=open("list.txt")
        counting = 1 + int(f.read())
        f.close()
        print("pomodoro added by 1")
        f=open("list.txt","w")
        f.write(str(counting))
        f.close()
        print("\n\n\n")

    elif choice==3:
        os.system('CLS')
        print("showing pomodoro")
        f = open("list.txt")
        print(f.read()+" pomodoro already do")
        f.close()
        print("\n\n\n")

    elif choice==4:
        break;


    
print("Byee .....")
print("Thanks and good luck ^^")