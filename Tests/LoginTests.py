from controllers.LoginController import LoginController
from models.User import User
from models.Role import Role
from models.PasswordFileManager import PasswordFileManager

loginController = LoginController()

testUser = User("TestId", "TestId", Role.CLIENT)
testPswd = "!Password123!"

def runAllLoginTests():
    print("Running Enrollment Tests...\n")
    enrollTestUser()
    testLoginUser()
    testWrongPassword()
    testWithNonExistantUser()

def enrollTestUser():
    result = loginController.createAccount(testUser.getUserId(), testPswd, testUser.getRole(), testUser.getNickname())
    assert(result == True)

def testLoginUser():
    print("Testing login with test user...")

    result, loggedInUser = loginController.login(testUser.getUserId(), testPswd)

    print("Expected Result: True, Actual: " + str(result))
    assert(result == True)
    assert(loggedInUser.getNickname() == testUser.getNickname())
    print()

def testWrongPassword():
    print("Testing login with test user by incorrect password...")

    result, loggedInUser = loginController.login(testUser.getUserId(), "Incorrect")

    print("Expected Result: False, Actual: " + str(result))
    assert(result == False)
    assert(loggedInUser == None)
    print()

def testWithNonExistantUser():
    print("Testing login with unknown user...")

    result, loggedInUser = loginController.login("Random", "Incorrect")

    print("Expected Result: False, Actual: " + str(result))
    assert(result == False)
    assert(loggedInUser == None)
    print()

    passwdManager = PasswordFileManager()
    passwdManager.deleteRecordByUserId(testUser.getUserId())
