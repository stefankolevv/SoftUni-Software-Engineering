class Profile:
    def __init__(self, username, password):
        self.__username = self.__validate_username(username)
        self.__password = self.__validate_password(password)

    def __validate_username(self, username):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        return username

    def __validate_password(self, password):
        if not (len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password)):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        return password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'