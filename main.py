import auth


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "l": self.login,
            "c": self.add_user,
            "q": self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Taki uzytkownik nie istnieje...")
            except auth.InvalidPassword:
                print("Nieprawidlowe haslo...")
            else:
                self.username = username

    def add_user(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.add_user(username, password)
            except auth.UsernameAlreadyExist:
                print("Taki uzytkownik juz istnieje..")
            except auth.PasswordTooShort:
                print("Haslo musi zawierac min 4 znaki..")
            else:
                print("Nowy uzytkownik zostal dodany.")
                Editor().menu()

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
        Please enter a command:
        \tl -\tLogin
        \tc -\tAdd User
        \tq -\tQuit
        """)
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing auth module")


Editor().menu()
