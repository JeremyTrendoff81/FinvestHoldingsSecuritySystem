import re

class ProactivePasswordChecker:
    """The Proactive password checker should check if a password is strong enough to be entered into the system."""

    def __init__(self) -> None:
        """
        Using the 2020-200 _most_used_passwords wordlist from https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt
        and the banned passwords outlined in the assignment description, initialize the bannedPasswords list. To add more, add more lines to the BannedPasswords text file
        in System Resources. 
        """
        self._bannedPasswords = []

        with open("system-resources/BannedPasswords.txt", "r") as file:
            for passwd in file:
                self._bannedPasswords.append(passwd.strip())
    
    def validatePassword(self, userId: str, password: str) -> bool:
        """Validate the password the user wishes to enter.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if strong enough. False, otherwise.
        """
        if password in self._bannedPasswords:
            return False

        if len(password) < 8:
            return False
        
        if password == userId:
            return False
        
        uppercase, lowercase, numerical, special = False, False, False, False

        specialCharacters = ["!", "@", "#", "$", "%", "?", "*"]

        for character in password:
            if character.isupper():
                uppercase = True
            elif character.isdigit():
                numerical = True
            elif character in specialCharacters:
                special = True
            elif character.islower():
                lowercase = True
            
            if uppercase and lowercase and numerical and special:
                return self._validateFormat(password)
        
        return False
    
    def _validateFormat(self, password: str) -> bool:
        return not (self._isLicensePlateFormat(password) or self._isCalenderDateFormat(password) or self._isTelephoneNumberFormat(password))
    
    def _isLicensePlateFormat(self, password: str) -> bool:
        reg = "[a-zA-Z]{4}-[0-9]{3}"
        licensePlateFormat = re.compile(reg)
        return re.search(licensePlateFormat, password)
    
    def _isCalenderDateFormat(self, password: str) -> bool:
        # format from https://stackoverflow.com/questions/4709652/python-regex-to-match-dates
        reg = "^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$"
        dateFormat = re.compile(reg)
        return re.search(dateFormat, password)
    
    def _isTelephoneNumberFormat(self, password: str) -> bool:
        # format from https://www.abstractapi.com/guides/phone-number-python-regex
        reg = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
        telephoneNumberFormat = re.compile(reg)
        return re.search(telephoneNumberFormat, password)
    

    