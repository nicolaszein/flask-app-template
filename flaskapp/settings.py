import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
DATABASE_URL = os.getenv('DATABASE_URL', '')
