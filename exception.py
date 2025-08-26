class UserNotFoundException(Exception):
    detail = "User not found"

class WrongPasswordException(Exception):
    detail = "Wrong password"

class TokenExpiredException(Exception):
    detail = "Token expired"

class TokenNotCorrectException(Exception):
    detail = "Token not correct"