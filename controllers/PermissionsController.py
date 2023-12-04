from models.ReferenceMonitor import ReferenceMonitor
from models.PasswordFileManager import PasswordFileManager
from models.User import User

class PermissionsController:
    """The PermissionsController class will be responsible for retrieving user permissions from the reference monitor."""

    def __init__(self) -> None:
        self._referenceMonitor = ReferenceMonitor()
        self._passwordFileManager = PasswordFileManager()

    def _accountExists(self, userId: str) -> bool:
        """Check if Account Already Exists.

        Args:
            userId (str): The user id to check for.

        Returns:
            bool: True if account exists, false otherwise.
        """
        if self._passwordFileManager.retrieveRecordFromFileByUserId(userId) != []:
            return True
        return False
    
    def getUserPermissions(self, user: User) -> list:
        """Get a user's permissions.

        Args:
            user (User): The User whose permissions you'd like to fetch.

        Returns:
            list: A list of string tuples formatted (Action Name, Read/Write Permissions)
        """
        if self._accountExists(user.getUserId()):
            return self._referenceMonitor.getPermissionsForRole(user.getRole())
        else:
            return []
