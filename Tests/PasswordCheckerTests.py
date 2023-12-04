from models.ProactivePasswordChecker import ProactivePasswordChecker

passwdChecker = ProactivePasswordChecker()

def runPasswordCheckerTests():
    print("Running Password Checker Tests...\n")
    testValidPassword()
    testPasswordEqualsUserId()
    testPasswordFromBannedPasswordList()
    testPasswordTooSmall()
    testPasswordNoUpperCase()
    testPasswordNoLowerCase()
    testPasswordNoNumber()
    testPasswordNoSpecialCharacter()
    testPasswordWithNoSpecialCharacterFromSet()
    testPasswordInDateFormat()
    testPasswordInLicensePlateFormat()
    testPasswordInPhoneNumberFormat()

def testValidPassword():
    print("Test a valid password...")

    testPassword = "12*yuiH7"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: True, Actual Result: " + str(result))
    assert(result == True)

    print()

def testPasswordEqualsUserId():
    print("Test password equals user id...")

    testPassword = "testId"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordFromBannedPasswordList():
    print("Testing the banned password Qwerty123!...")

    testPassword = "Qwerty123!"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordTooSmall():
    print("Testing the short password *Yu4...")

    testPassword = "*Yu4"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordNoUpperCase():
    print("Testing password with no uppercase: *67mn5h!")

    testPassword = "*67mn5h!"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordNoLowerCase():
    print("Testing password with no lowercase: *67MN5H!")

    testPassword = "*67MN5H!"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordNoNumber():
    print("Testing password with no number: *AB!mN!5H!")

    testPassword = "*AB!MN!5H!"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordNoSpecialCharacter():
    print("Testing password with no special character: AB3m3N5H")

    testPassword = "*AB!MN!5H!"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordWithNoSpecialCharacterFromSet():
    print("Testing password with no special character in specified set: &AB3m3N5H")

    testPassword = "&AB3m3N5H"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordInDateFormat():
    print("Testing password in date format: !!3mN1920/12/12")

    testPassword = "&AB3m3N5H"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordInLicensePlateFormat():
    print("Testing password in license plate format: !!3mNABCD-12312/12")

    testPassword = "!!3mNABCD-12312/12"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()

def testPasswordInPhoneNumberFormat():
    print("Testing password in license plate format: !!3mN647-555-555512/12")

    testPassword = "!!3mNABCD-12312/12"
    result = passwdChecker.validatePassword("testId", testPassword)
    
    print("Expected Result: False, Actual Result: " + str(result))
    assert(result == False)

    print()