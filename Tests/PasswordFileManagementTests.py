from models.PasswordFileManager import PasswordFileManager

passwdManager = PasswordFileManager()

def runPasswdManagementTests():
    print("Running Password Management Tests...\n")
    testAddRetrieveAndDeleteRecord()
    testComparisonOfPlaintextAndHashedPasswords()


def testAddRetrieveAndDeleteRecord():
    print("Testing adding and retrieving a record...")

    testUserId = "Test"
    testPasswd = "Test123"

    passwdManager.writeToFile(testUserId, testPasswd)

    record = passwdManager.retrieveRecordFromFileByUserId(testUserId)

    print("Expected User Id: " + testUserId)
    print("Actual User Id: " + str(record[0]))
    assert(record[0] == testUserId)

    passwdManager.deleteRecordByUserId(testUserId)
    record = passwdManager.retrieveRecordFromFileByUserId(testUserId)
    assert(record == [])

def testComparisonOfPlaintextAndHashedPasswords():
    print("Testing comparison of plaintext and hashed passwords...")

    testUserId = "Test"
    testPasswd = "Test123"

    passwdManager.writeToFile(testUserId, testPasswd)

    hashedPassword = passwdManager.retrievePasswordByUserId(testUserId)

    assert(passwdManager.comparePasswords(testPasswd, hashedPassword) == True)

    passwdManager.deleteRecordByUserId(testUserId)


