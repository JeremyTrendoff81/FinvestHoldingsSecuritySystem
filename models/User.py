from models.Role import Role 

class User:
    """
    A User in the System. 
    """

    def __init__(self, username: str, nickname: str, role: Role) -> None:
        """
        Constructor. Build a user with a username, nickname, and a given role. 

        Args:
            username (str): The user's username. 
            nickname (str): The user's nickname.
            role (Role): The Role the user shall have. 
        """

        self._username = username
        self._nickname = nickname
        self._role = role

    def getUsername(self) -> str:
        return self._username
    
    def getNickname(self) -> str:
        return self._nickname
    
    def getRole(self) -> Role:
        return self._role
    
     