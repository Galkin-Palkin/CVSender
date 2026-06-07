import os
from dotenv import load_dotenv


load_dotenv()

CV_STORAGE_PATH = os.getenv("CV_STORAGE_PATH")
ALLOWED_MIME_TYPES = os.getenv("ALLOWED_MIME_TYPES").split(', ')
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(', ')
#TODO: Написать как узнать свой id в README
ALLOWED_USER_ID = os.getenv("ALLOWED_USER_ID")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_DIR = os.path.join(ROOT_DIR, CV_STORAGE_PATH)

LETTER_ID = "letter_id"
TITLE_ID = "title_id"