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
        with open("System Resources/PermissionsMatrix.csv", "r") as CSVFile:
            CSVreader = csv.DictReader(CSVFile)
            data = [row for row in CSVreader]
            matrixDictonary = {}

            print(data)

            for item in data:
                role = item.pop("Role")
                matrixDictonary[role] = item
        self._permissionsMatrix = matrixDictonary

        print(self._permissionsMatrix)

    def getPermissionsForRole(self, role: Role) -> list:
        permissionsList = []

        if (role in self._permissionsMatrix):
            for permission in self._permissionsMatrix.get(role):
                return               