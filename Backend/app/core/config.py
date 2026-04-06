import os
from dotenv import load_dotenv

load_dotenv()   # loads .env file

DATABASE_URL = os.getenv("DATABASE_URL")
import os 

from dotenv import load_dotenv 
load_dotenv()   

# loads .env file
DATABASE_URL = os.getenv("DATABASE_URL")