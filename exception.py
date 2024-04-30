class UserNotFoundException(Exception):
    detail = "User not found"

class UserNotCorrentPasswordException(Exception):
    detail = "User not corrent password"

class TokenExpireException(Exception):
    detail = "Token expire"

class TokenNotCorrectException(Exception):
    detail = "Token not correct"