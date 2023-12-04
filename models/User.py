from models.Role import Role 

class User:
    """
    A User in the System. 
    """

    def __init__(self, userId: str, nickname: str, role: Role) -> None:
        """
        Constructor. Build a user with a userId, nickname, and a given role. 

        Args:
            userId (str): The user's Id. 
            nickname (str): The user's nickname.
            role (Role): The Role the user shall have. 
        """

        self._userId = userId
        self._nickname = nickname
        self._role = role

    def getUserId(self) -> str:
        """
        Get the User's Id 
        Returns:
            str: The User's Id
        """
        return self._userId
    
    def getNickname(self) -> str:
        """Get the nickname of the user. 

        Returns:
            str: The User's nickname.
        """
        return self._nickname
    
    def getRole(self) -> Role:
        """Get the user's role.

        Returns:
            Role: The role of the user.
        """
        return self._role
    
     