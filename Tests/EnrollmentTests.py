from controllers.LoginController import LoginController
from models.User import User
from models.Role import Role
from models.PasswordFileManager import PasswordFileManager

loginController = LoginController()

def runAllEnrollmentTests():
    print("Running Enrollment Tests...\n")
    testEnrollUser()
    testEnrollExistingUser()

def testEnrollUser():
    print("Testing Enrollment of a test user...")

    testUser = User("TestId", "TestId", Role.CLIENT)
    testPswd = "!Password123!"

    result = loginController.createAccount(testUser.getUserId(), testPswd, testUser.getRole(), testUser.getNickname())

    print("Expected Result: True, Actual: " + str(result))
    assert(result == True)
    assert(loginController.accountAlreadyExists(testUser.getUserId()))

    print()

def testEnrollExistingUser():
    print("Testing Enrollment of a user that is already in the system...")

    testUser = User("TestId", "TestId", Role.CLIENT)
    testPswd = "!Password123!"

    result = loginController.createAccount(testUser.getUserId(), testPswd, testUser.getRole(), testUser.getNickname())

    print("Expected Result: False, Actual: " + str(result))
    assert(result == False)

    passwdManager = PasswordFileManager()
    passwdManager.deleteRecordByUserId(testUser.getUserId())

    print()



