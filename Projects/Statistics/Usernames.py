
#program for Computer Usernames

def main():
    #input user's names,
    firstName=input("Enter Your First Name: ").lower()
    lastName=input("Enter Last Name: ").lower()
    uname=firstName[0]+lastName[:7]

    #output Username,
    print("Your Username Is ", uname)

main()
