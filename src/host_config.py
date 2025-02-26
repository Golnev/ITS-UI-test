import os

from dotenv import load_dotenv

load_dotenv()
HOSTS = {
    "test": "https://thinking-tester-contact-list.herokuapp.com/",
    "dev": "",
    "prod": "",
}

__env = os.getenv("ENV", "test")
base_url: str = HOSTS[__env]
