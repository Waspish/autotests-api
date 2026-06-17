from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS service"
    BILLING = "Billing service"
    ANALYTICS = "Analytics service"
