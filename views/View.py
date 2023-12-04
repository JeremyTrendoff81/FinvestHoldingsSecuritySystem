from controllers.LoginController import LoginController
from controllers.PermissionsController import PermissionsController
from models.Role import Role
from models.User import User
import datetime

class View:
    """The view class to hold the system views."""

    def __init__(self) -> None:
        self._loginController = LoginController()
        self._permissionsController = PermissionsController()
    
    def renderView(self):
        """The main view renderer."""

        print("\nFinvest Holdings")
        print("Client Holdings and Information System")
        print("----------------------------------------------")
        userId = input("Enter Username: ")

        if self._loginController.accountAlreadyExists(userId):
            self.loginView(userId)
        else:
            self.enrollmentView(userId)
    
    def loginView(self, userId: str):
        """The login view. 

        Args:
            userId (str): The userId to attempt login with.
        """
        password = input("Enter Your password: ")
        accessGranted, user = self._loginController.login(userId, password)

        if not accessGranted:
            print("ACCESS DENIED")
            self.renderView()
            return

        if user.getRole() == Role.TELLER:
            print("\nTeller's can only access the system from 9am to 5pm (or 09:00:00 to 17:00:00)...")

            currentTime = datetime.datetime.now().time()

            # currentTime = datetime.time(11, 0, 0) # For Testing after working hours...

            print("It is currently: " + str(currentTime))

            startTime = datetime.time(9, 0, 0)
            endTime = datetime.time(17, 0, 0)

            if ((currentTime <= startTime) or (currentTime >= endTime)):
                print("You should not have access, however, for testing purposes, you may override this...")
                override = input("Would you like too? Y or N: ")
                if override == 'Y' or 'y':
                    accessGranted = True
                else:
                    print("ACCESS DENIED")
                    return
                

        if (accessGranted):
            print("ACCESS GRANTED\n")
            print("User Id: " + user.getUserId())
            print("Nickname: " + user.getNickname())
            print("Role: " + user.getRole().value)
            print("\nPermissions: ")

            permissions = self._permissionsController.getUserPermissions(user)

            for (action, permission) in permissions:
                print("-> " + action + ": " + permission)
        
        
    def enrollmentView(self, userId: str):
        """The enrollment view.

        Args:
            userId (str): The userId to attempt enrollment with.
        """
        password = input("Select Your password: ")

        nickname = input("Select Your Nickname: ")

        print("Select Your Role: \n")
        print("Client: 1")
        print("Premium Client: 2")
        print("Financial Planner: 3")
        print("Financial Advisor: 4")
        print("Investment Analyst: 5")
        print("Technical Support: 6")
        print("Teller: 7")
        print("Compliance Officer: 8")

        roleNum = input(": ")

        roleOptions = {"1" : Role.CLIENT,
                       "2" : Role.PREMIUM_CLIENT,
                       "3" : Role.FINANCIAL_PLANNER,
                       "4" : Role.FINANCIAL_ADVISOR,
                       "5" : Role.INVESTMENT_ANALYST,
                       "6" : Role.TECHNICAL_SUPPORT,
                       "7" : Role.TELLER,
                       "8" : Role.COMPLIANCE_OFFICER}
        
        if roleNum not in roleOptions.keys():
            print("Bad Role Selection! Please Ensure You Type a Valid Number!")
            self.renderView()
        
        role = roleOptions[roleNum]

        accessGranted = self._loginController.createAccount(userId, password, role, nickname)

        if (not accessGranted):
            print("\nPassword Too Weak!")
            print("Password must: ")
            print("- be at least 8 characters long.")
            print("- contain one uppercase letter.")
            print("- contain one lowercase letter.")
            print("- contain one number.")
            print("- contain one special character: {!, @, #, $, %, *, ?}")
            print("- not contain a calendar date i.e. 12/12/1900")
            print("- not contain a license plate number i.e. ABCD-123")
            print("- not contain a phone number i.e. 555-555-5555")
            self.renderView()
            return

        self.renderView()

        
    
