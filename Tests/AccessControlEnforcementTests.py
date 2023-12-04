from controllers.LoginController import LoginController
from models.User import User
from models.Role import Role
from models.PasswordFileManager import PasswordFileManager
from controllers.PermissionsController import PermissionsController

loginController = LoginController()
permissionsController = PermissionsController()

testUser = User("TestId", "TestId", Role.CLIENT)
testPswd = "!Password123!"

def runAllAccessControlEnforcementTests():
    print("Running Access Control Enforcement Tests...\n")
    enrollTestUser()
    testEnsureUserHasCorrectPermissions()
    testInvalidUserHasNoPermissions()

def enrollTestUser():
    result = loginController.createAccount(testUser.getUserId(), testPswd, testUser.getRole(), testUser.getNickname())
    assert(result == True)

def testEnsureUserHasCorrectPermissions():
    print("Testing that the test user has correct permissions...\n")

    userPermissions = permissionsController.getUserPermissions(testUser)
    expectedPermissions = [('Personal Account Balance', 'Read'), ('Personal Investment Portfolio', 'Read'), ('Advisor Contact Details', 'Read')]

    print("Expected Permissions: " + str(expectedPermissions))
    print("Actual Permissions: " + str(userPermissions))
    assert(userPermissions == expectedPermissions)
    print()

def testInvalidUserHasNoPermissions():
    print("Testing that an invalid user has no permissions...\n")

    userPermissions = permissionsController.getUserPermissions(User("Test", "Test", Role.CLIENT))

    print("Expected Permissions: " + str([]))
    print("Actual Permissions: " + str(userPermissions))
    assert(userPermissions == [])

    passwdManager = PasswordFileManager()
    passwdManager.deleteRecordByUserId(testUser.getUserId())
    print()
