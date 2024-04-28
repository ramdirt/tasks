class UserNotFoundException(Exception):
    detail = "User not found"

class UserNotCorrentPasswordException(Exception):
    detail = "User not corrent password"