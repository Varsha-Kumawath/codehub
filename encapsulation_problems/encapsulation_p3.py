import string

class PasswordManager:

    def __init__(self):
        self.username="none"
        self.__password="none"

    def add_new_password(self,username,password):
        if (len(password)<8 ):
            print("Password should have minimum 8 characters")
            return

        if not any(char.isdigit() for char in password):
            print("Password should contains a number")
            return

        if not any (char in string.punctuation for char in password):
            print("Password should contains a  special character ")
            return

        self.__password = password
        self.username = username
        print(self.username)
        print(self.__password)
        print("successfully added the credentials")

    @property
    def masked_password(self):
        if self.__password :  # Checks if password is not empty or None
           return f"username : {self.username} and Password :{'*' * (len(self.__password)-4)} {self.__password[-4:]}"
        else:
          print("no records found")

pm=PasswordManager()
pm.add_new_password('vj','Varsha1057@#')
print(pm.masked_password)
