from models.Role import Role
from models.ReferenceMonitor import ReferenceMonitor

reference_monitor = ReferenceMonitor()

def runAccessControlTests():
    print("Running Access Control Tests...\n")
    testClient()
    testPremiumClient()
    testAdvisor()
    testPlanner()
    testAnalyst()
    testSupport()
    testTeller()
    testComplianceOfficer()
    testInvalidRole()

def testClient(): 
    print("Testing Permission Assignment for Client Role")

    expected_permissions = [('Personal Account Balance', 'Read'), ('Personal Investment Portfolio', 'Read'), ('Advisor Contact Details', 'Read')]
    permissions = reference_monitor.getPermissionsForRole(Role.CLIENT.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testPremiumClient(): 
    print("Testing Permission Assignment for Premium Client Role")

    expected_permissions = [('Personal Account Balance', 'Read'), ('Personal Investment Portfolio', 'Read and Write'), ('Advisor Contact Details', 'Read'), ('Planner Contact Details', 'Read'), ('Analyst Contact Details', 'Read')]
    permissions = reference_monitor.getPermissionsForRole(Role.PREMIUM_CLIENT.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testPlanner(): 
    print("Testing Permission Assignment for Financial Planner Role")

    expected_permissions = [('Client Account Balance', 'Read'), ('Client Investment Portfolio', 'Read and Write'), ('Money Market Instruments', 'Read'), ('Private Consumer Instruments', 'Read')]
    permissions = reference_monitor.getPermissionsForRole(Role.FINANCIAL_PLANNER.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testAdvisor(): 
    print("Testing Permission Assignment for Financial Advisor Role")

    expected_permissions = [('Client Account Balance', 'Read'), ('Client Investment Portfolio', 'Read and Write'), ('Private Consumer Instruments', 'Read')]
    permissions = reference_monitor.getPermissionsForRole(Role.FINANCIAL_ADVISOR.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testAnalyst(): 
    print("Testing Permission Assignment for Investment Analyst Role")

    expected_permissions = [('Client Account Balance', 'Read'), ('Client Investment Portfolio', 'Read and Write'), ('Money Market Instruments', 'Read'), ('Private Consumer Instruments', 'Read'), ('Derivatives Trading', 'Read')]
    permissions = reference_monitor.getPermissionsForRole(Role.INVESTMENT_ANALYST.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testSupport(): 
    print("Testing Permission Assignment for Technical Support Role")

    expected_permissions = [('View Client Information', 'Read'), ('Request Client Account Access', 'Read and Write')]
    permissions = reference_monitor.getPermissionsForRole(Role.TECHNICAL_SUPPORT.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testTeller(): 
    print("Testing Permission Assignment for Teller Role")

    expected_permissions = [('Client Account Balance', 'Read')]
    permissions = reference_monitor.getPermissionsForRole(Role.TELLER.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testComplianceOfficer(): 
    print("Testing Permission Assignment for Compliance Officer Role")

    expected_permissions = [('Client Account Balance', 'Read'), ('Validate Investment Portfolio Modifications', 'Read and Write')]
    permissions = reference_monitor.getPermissionsForRole(Role.COMPLIANCE_OFFICER.value)

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()

def testInvalidRole():
    print("Testing Permission Assignment for Invalid Role")

    expected_permissions = []
    permissions = reference_monitor.getPermissionsForRole("Invalid")

    print("Expected: " + str(expected_permissions))
    print("Actual: " + str(permissions))

    assert(expected_permissions == permissions)

    print()
