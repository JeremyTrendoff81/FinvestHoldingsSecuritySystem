from enum import Enum

class Role(Enum):
    """
    The set of roles that users can be assigned.

    Args:
        Enum (String)
    """

    CLIENT = "Client",
    PREMIUM_CLIENT = "Premium Client",
    FINANCIAL_PLANNER = "Financial Planner",
    FINANCIAL_ADVISOR = "Financial Advisor",
    INVESTMENT_ANALYST = "Investment Analyst",
    TECHNICAL_SUPPORT = "Technical Support",
    TELLER = "Teller",
    COMPLIANCE_OFFICER = "Compliance Officer"