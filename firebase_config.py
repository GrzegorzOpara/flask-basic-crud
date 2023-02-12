import os
from dotenv import load_dotenv

load_dotenv()

config = {
  "apiKey": os.getenv('FB_APIKEY'),
  "authDomain": os.getenv('FB_AUTHDOMAIN'),
  "databaseURL": os.getenv('FB_DATABASEURL'),
  "storageBucket": os.getenv('FB_STORAGEBUCKET'),
}