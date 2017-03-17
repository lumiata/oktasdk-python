class UserProfile:
    types = {
        'login': str,
        'email': str,
        'secondEmail': str,
        'firstName': str,
        'lastName': str,
        'mobilePhone': str,
        'userType': str,
        'organization': str,
        'nickName': str
    }

    def __init__(self):
        self.login = None  # str
        self.email = None  # str
        self.secondEmail = None  # str
        self.firstName = None  # str
        self.lastName = None  # str
        self.mobilePhone = None  # str
        self.organization = None # str
        self.userType = None # str
        self.nickName = None # str
