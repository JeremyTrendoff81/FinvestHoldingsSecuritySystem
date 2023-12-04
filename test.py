from Tests import AccessControlTests as acTests
from Tests import PasswordFileManagementTests as pfmTests

def runTests():
    print("!--------TOTAL TEST SUITE---------!")
    acTests.runAccessControlTests()
    pfmTests.runPasswdManagementTests()

runTests()