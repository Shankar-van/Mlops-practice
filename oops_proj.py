class chatbook:
    
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""" Wellcome to chatbook !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 1 to write a post
                           4. press 4 to message a Friend 
                           5. press any other key to exit \n""""")   
        if user_input == "1" :
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        pwd = input("setup your password here ->")
        self.username = email
        self.password = pwd
        print("you have signed up sucessfully !!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username =='' and self.password == '':
            print("please sign up first by pressing 1 in the main menu ")
        else:
            uname = input("enter your email/username here -> ")
            pwd =  input("Enteryour password here -> ")
            if self.username == uname and self.password == pwd:
                print("you Have signedin sucessfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials...")
        print("\n")
        self.menu()

obj = chatbook()
