import bcrypt
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

            # bcrypt encryption examples: https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
            bytes = password.encode('utf_8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)

            file.write(userId + ":" + str(hash.decode()) + ":" + role.value + ":" + nickname + "\n")
            file.close()
        except:
            return
    
    def retrieveRecordFromFileByUserId(self, userId: str) -> list:
        """Retrieve a whole record from the password file.

        Args:
            userId (_type_): The record to retrieve.

        Returns:
            list: The record as a list. User ID: index 0, Password: index 1, Role: index 2, Nickname: index 3.
        """
        try: 
            file = open(self._passwdFilePath, "r")

            for record in file:
                data = record.split(":")
                if (data[0] == userId):
                    data[2] = Role(data[2])
                    data[3] = data[3].strip()
                    file.close()
                    return data
        
            file.close()
            return []
        except: 
            print("Error!")
            return None
    
    def comparePasswords(self, plaintext: str, hashed: str) -> bool:
        """Return if the plaintext and the hashed passwords are the same. 

        Returns:
            _type_: _description_
        """    
        return bcrypt.checkpw(plaintext.encode('utf-8'), hashed.encode())
    
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