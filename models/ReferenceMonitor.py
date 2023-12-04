import csv
from models.Role import Role

class ReferenceMonitor:
    """
    The Reference Monitor will be responsible for retrieving a User's permissions from the permission matrix upon login. 
    """

    def __init__(self) -> None:
        """
        Constructor. Retrieves the permissions matrix from system resources. 
        """

        with open("System Resources/PermissionsMatrix.csv", "r") as matrixCSV:
            reader = csv.DictReader(matrixCSV)
            data = [row for row in reader]
            matrixDictonary = {}

            for item in data:
                role = item.pop("Role")
                matrixDictonary[role] = item
        self._permissionsMatrix = matrixDictonary

    def getPermissionsForRole(self, role: Role) -> list:
        permissionsList = []

        if (role in self._permissionsMatrix):
            for permission in self._permissionsMatrix.get(role):
                if ('RW' in self._permissionsMatrix.get(role)[permission]):
                    permissionsList.append((permission, "Read and Write"))
                elif('R' in self._permissionsMatrix.get(role)[permission]):
                    permissionsList.append((permission, "Read"))
                elif('W' in self._permissionsMatrix.get(role)[permission]):
                    permissionsList.append((permission, "Write"))
        
        return permissionsList