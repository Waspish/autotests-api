import time
import uuid


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


def get_uuid4() -> str:
    return str(uuid.uuid4())
