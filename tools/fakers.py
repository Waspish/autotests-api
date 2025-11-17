import time
import uuid


def get_random_email() -> str:
    return f"test.{time.time_ns()}@example.com"


def get_uuid4() -> str:
    return str(uuid.uuid4())
