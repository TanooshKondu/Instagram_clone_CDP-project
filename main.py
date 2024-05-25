#https://pastebin.com/b2u3VzH7
#https://pastebin.com/HL90vAgB
class User:
    def __init__(self, userName, password, fullName):
        self.userName = userName
        self.password = password
        self.fullName = fullName
        self.followers = []
        self.following = []
        self.followRequestsSent = []
        self.followRequestsSent=[]
        self.followRequestsReceived = []
dataStore = {}

def displayMainMenu():
    print("--------------------------------------------------")
    print("1 - Put follow request")
    print("2 - Accept follow request")
    print("3 - Post Something")
    print("4 - Logout")
    option = int(input("Choose the option: "))
    print("--------------------------------------------------")
    
    if option == 1:
        print("Handle")
    elif option == 2:
        print("Handle")
    elif option == 3:
        print("Handle")
    elif option == 4:
        print("Handle")
    else:
        print("")
        exit(0)




def handleLogin():
    print("Enter your login details")
    userName = input("Enter your user-name: ")
    password = input("Enter your password: ")
    if userName not in dataStore:
        print("userName not present, Create an Account")
    else:
        print("Logged-in Successfully")
        displayMainMenu()
        
    
def handleSignUp():
    print("Enter your details to create an account")
    fullName = input("Enter your full-name: ")
    userName = input("Enter your user-name: ")
    password = input("Enter your password: ")
    if userName not in dataStore:
        newUser = User(userName, password, fullName)
        dataStore[userName] = newUser
        print("Account created Successfully")
    else:
        print("User-Name already exists")
    
while True:
    print("--------------------------------------------------")
    print("1-Login")
    print("2-SignUp")
    print("3-Exit")
    option = int(input("Choose the option: "))
    print("--------------------------------------------------")
    
    if option == 1:
        handleLogin()
    elif option == 2:
        handleSignUp()
    else:
        print("Thank you for using Instagram")
        exit(0)