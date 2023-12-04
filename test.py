from tests import AccessControlTests as acTests
from tests import PasswordFileManagementTests as pfmTests
from tests import PasswordCheckerTests as pcTests
from tests import EnrollmentTests as eTests
from tests import LoginTests as lTests
from tests import AccessControlEnforcementTests as aceTests

def runTests():
    print("!--------TOTAL TEST SUITE---------!")
    acTests.runAccessControlTests()
    pfmTests.runPasswdManagementTests()
    pcTests.runPasswordCheckerTests()
    eTests.runAllEnrollmentTests()
    lTests.runAllLoginTests()
    aceTests.runAllAccessControlEnforcementTests()

runTests()