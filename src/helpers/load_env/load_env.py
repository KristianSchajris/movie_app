import os
from dotenv import load_dotenv

class LoadEnv:
    _instances = {}

    def __new__(cls, key: str):
        if key not in cls._instances:
            instance = super(LoadEnv, cls).__new__(cls)
            load_dotenv()
            instance.value = os.getenv(key)
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, key: str) -> None:
        if not hasattr(self, 'initialized'):
            self.key = key
            self.initialized = True

    def get_value(self) -> str:
        return self.value
