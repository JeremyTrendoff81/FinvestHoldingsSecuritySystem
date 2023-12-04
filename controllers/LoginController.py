from models.PasswordFileManager import PasswordFileManager
from models.ProactivePasswordChecker import ProactivePasswordChecker
from models.Role import Role
from models.User import User

class LoginController:
    """The LoginController to handle login and account creation operations."""

    def __init__(self) -> None:
        self._passwordFileManager = PasswordFileManager()
        self._passwordChecker = ProactivePasswordChecker()
    
    def accountAlreadyExists(self, userId: str) -> bool:
        """Check if Account Already Exists.

        Args:
            userId (str): The user id to check for.

        Returns:
            bool: True if account exists, false otherwise.
        """
        if self._passwordFileManager.retrieveRecordFromFileByUserId(userId) != []:
            return True
        return False
    
    def createAccount(self, userId: str, password: str, role: Role, nickname: str) -> bool:        
        """Create an account on the system.

        Args:
            userId (str): The userId to add
            password (str): The password to check and hash.
            role (Role): The user's Role. 
            nickname (str): The user's nickname.

        Returns:
            bool: True if account created was successful, false otherwise.
        """
        if self.accountAlreadyExists(userId):
            return False

        if self._passwordChecker.validatePassword(userId, password):
            self._passwordFileManager.writeToFile(userId, password, role, nickname)
            return True
        return False 

    def login(self, userId: str, password: str) -> (bool, User):
        """Login to the system.

        Args:
            userId (str): The userId to check
            password (str): The password to check.

        Returns:
            (bool, User): (If login was successful, The User that logged in)
        """
        if not self.accountAlreadyExists(userId):
            return (False, None)

        record = self._passwordFileManager.retrieveRecordFromFileByUserId(userId)

        if self._passwordFileManager.comparePasswords(userId, password): 
            user = User(userId, record[4], record[3])
            return (True, user) 
        
        return (False, None)
