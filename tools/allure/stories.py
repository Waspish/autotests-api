from enum import Enum


class AllureStory(str, Enum):
    LOGIN = "Login"
    CREATE_ENTITY = "Create entity"
    DELETE_ENTITY = "Delete entity"
    UPDATE_ENTITY = "Update entity"
    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    VALIDATE_ENTITY = "Validate entity"
