class UserNotFoundException(Exception):
    detail = "User not found"

class WrongPasswordException(Exception):
    detail = "Wrong password"