class chatbook:
    
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = ''
        self.menu()

    def menu(self):
        user_input = input("""" Wellcome to chatbook !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 1 to write a post
                           4. press 4 to message a Friend 
                           5. press any other key to exit \n""""")   
        if user_input == "1" :
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


obj = chatbook()
