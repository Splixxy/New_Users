# imports datetime and os.path modules
import datetime
import os.path
# creates the date & time to be used later on
dt = datetime.datetime.now()
date = dt.strftime("%c")
date = str(date)
# checks if the setup.txt file exists
isF = os.path.isfile("setup.txt")
isF = str(isF)

# creates the main code of the program
def main():
    # opens setup.txt file as read
    setup = open("setup.txt","r")
    setupR = setup.read()
    # checks if 0 is in setup.txt if it is it does the below code
    if "0" in setupR:
        fUsersOpen = open("/etc/passwd","r")
        fUsersRead = fUsersOpen.read()
        fCheck = open("UserCheck.txt","a")
        fCheck.write(fUsersRead)
        fCheck.close()
        setup = open("setup.txt","w")
        setup.write("1")
        setup.close()
    # else if not 0 then it runs the below code to get the users from "/etc/passwd" and the
    # check against file
    else:
        fUsersOpen = open("/etc/passwd","r")
        fUsersRead = fUsersOpen.read()
        fCheck = open("UserCheck.txt","r")
        fCheckRead = fCheck.read()
        # checks if the files don't match, then it opens UserLog and says a new user has been added
        # with the date and time
        if fUsersRead != fCheckRead:
            flag = open("UserLog.txt","a")
            flag.write("\nA new user has been added to /etc/passwd on %s" % date)
            flag.close()
        # else if they do match it opens UserLog and says no new user with the date and time
        else:
            flag = open("UserLog.txt","a")
            flag.write("\nNo new user has been added as of %s" % date)
            flag.close()
# checks if the isfile == true and then runs the main function
if isF == "True":
    main()
# else if it doesn't exist it creates setup.txt and puts a 0 in it and then runs the main function
else:
    setup = open("setup.txt","a")
    setup.write("0")
    setup.close()
    main()
