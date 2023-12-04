import bcrypt
import os

class PasswordFileManager():
    """The PasswordFileManager Class will be responsible for password encryption and providing methods to add and retrieve records from the password file."""

    def __init__(self) -> None:
        self._passwdFilePath = "System Resources/passwd.txt"
    
    def writeToFile(self, userId: str, password: str):
        """Write a new record into the password file. 

        Args:
            userId (str): The user id to add. 
            password (str): the password to encrypt.
        """

        try:

            file = open(self._passwdFilePath, "a")

            # bcrypt encryption examples: https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
            bytes = password.encode('utf_8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)

            file.write(userId + ":" + str(hash.decode()) + "\n")
            file.close()

        except:
            return
    
    def retrieveRecordFromFileByUserId(self, userId) -> list:
        """Retrieve a whole record from the password file.

        Args:
            userId (_type_): The record to retrieve.

        Returns:
            list: The record as a list. User ID: index 0, Password: index 1.
        """
        try: 
            file = open(self._passwdFilePath, "r")

            for record in file:
                data = record.split(":")
                if (data[0] == userId):
                    data[1] = data[1].strip()
                    file.close()
                    return data
        
            file.close()
            return []
        
        except: 
            return []
    
    def retrievePasswordByUserId(self, userId) -> str:
        """Retrieve a password for a user id.

        Args:
            userId (_type_): The user's id.

        Returns:
            str: The hashed password.
        """
        try: 

            file = open(self._passwdFilePath, "r")

            for record in file:
                data = record.split(":")
                if (data[0] == userId):
                    file.close()
                    return data[1].strip()
            
            file.close()
            return ""
    
        except:
            return ""
    
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