import hashlib
import random
from models.Role import Role

class PasswordFileManager():
    """The PasswordFileManager Class will be responsible for password encryption and providing methods to add and retrieve records from the password file."""

    def __init__(self) -> None:
        self._passwdFilePath = "system-resources/passwd.txt"
    
    def writeToFile(self, userId: str, password: str, role: Role, nickname: str):
        """Write a new record into the password file. 

        Args:
            userId (str): The user id to add. 
            password (str): the password to encrypt.
            role (Role): The role of the user.
            nickname (str): The nickname of the User.
        """
        try:
            file = open(self._passwdFilePath, "a")

            salt = str(random.getrandbits(12))
            password = salt + password
            hashedPassword = hashlib.sha512(password.encode())

            file.write(userId + ":" + salt + ":" + hashedPassword.hexdigest() + ":" + role.value + ":" + nickname + "\n")
            file.close()
        except:
            return
    
    def retrieveRecordFromFileByUserId(self, userId: str) -> list:
        """Retrieve a whole record from the password file.

        Args:
            userId (_type_): The record to retrieve.

        Returns:
            list: The record as a list. User ID: index 0, Salt: index 1, Password: index 2, Role: index 3, Nickname: index 4.
        """
        try: 
            file = open(self._passwdFilePath, "r")

            for record in file:
                data = record.split(":")
                if (data[0] == userId):
                    data[3] = Role(data[3])
                    data[4] = data[4].strip()
                    file.close()
                    return data
        
            file.close()
            return []
        except: 
            print("Error!")
            return None
    
    def comparePasswords(self, userId: str, plaintext: str) -> bool:
        """Return if the plaintext and the hashed passwords are the same. 

        Returns:
            _type_: _description_
        """    
        record = self.retrieveRecordFromFileByUserId(userId)

        salt = record[1]
        storedPassword = record[2] 
        passwordToCompare = salt + plaintext
        passwordToCompareHashed = hashlib.sha512(passwordToCompare.encode())

        return storedPassword == passwordToCompareHashed.hexdigest()

        
    
    def deleteRecordByUserId(self, userId: str):
        """Delete a record from the passwd file.

        Args:
            userId (str): The user id to delete. 
        """
        try:
            with open(self._passwdFilePath , "r") as file:
                lines = file.readlines()
            
            with open(self._passwdFilePath, 'w') as file:
                for record in lines:
                    data = record.split(":")
                    if (data[0] != userId):  
                        file.write(record)
        except:
            return