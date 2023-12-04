from models.PasswordFileManager import PasswordFileManager
from models.Role import Role

passwdManager = PasswordFileManager()

def runPasswdManagementTests():
    print("Running Password Management Tests...\n")
    testAddRetrieveAndDeleteRecord()
    testComparisonOfPlaintextAndHashedPasswords()


def testAddRetrieveAndDeleteRecord():
    print("Testing adding and retrieving a record...")

    testUserId = "Test"
    testPasswd = "Test123"

    passwdManager.writeToFile(testUserId, testPasswd, Role.CLIENT, testUserId)

    record = passwdManager.retrieveRecordFromFileByUserId(testUserId)

    print("Expected User Id: " + testUserId)
    print("Actual User Id: " + str(record[0]))
    assert(record[0] == testUserId)

    print("Actual User Role: " + str(record[3]))
    assert(record[3] == Role.CLIENT)

    passwdManager.deleteRecordByUserId(testUserId)
    record = passwdManager.retrieveRecordFromFileByUserId(testUserId)
    assert(record == [])

    print()

def testComparisonOfPlaintextAndHashedPasswords():
    print("Testing comparison of plaintext and hashed passwords...")

    testUserId = "Test"
    testPasswd = "Test123"

    passwdManager.writeToFile(testUserId, testPasswd, Role.CLIENT, testUserId)

    print("Passwords are the same?: " + str(passwdManager.comparePasswords(testUserId, testPasswd)))
    assert(passwdManager.comparePasswords(testUserId, testPasswd) == True)

    passwdManager.deleteRecordByUserId(testUserId)

    print()


