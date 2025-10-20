class chatbook:

    __user_id = 0

    def __init__(self):
        self.__name = 'default User'
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        # self.userid = 0
        # self.userid += 1
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()


    @staticmethod
    def get_id():
        return chatbook.__user_id
    

    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def gget_name(self):
        return self.__name
    
    def sset_name(self,value):
        self.__name = value



    def menu(self):
        user_input = input("""" Wellcome to chatbook !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. press 4 to message a Friend 
                           5. press any other key to exit

                           -> """"")   
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
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
    
    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your Message Here ->")
            print(f"your are following Content has been Posted -> {txt}")
        else:
            print("You need to Signin first too post somethhing....")
        print("\n")
        self.menu()  



    def sendmsg(self):
        if self.loggedin == True:
             txt = input("Enter your Message Here ->")
             frnd = input("Whom to send the meessage -> ")
             print(f"Your messagee has been send to {frnd}")
        else:
            print("You need to Signin first too post somethhing....")
        print("\n")
        self.menu()  

             

# obj = chatbook()
