from enum import Enum


class AllureFeature(str, Enum):
    FILES = "Files"
    USERS = "Users"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"
