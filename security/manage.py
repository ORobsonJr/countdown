from os import getcwd
from pathlib import Path


def secret_key():
    """"
    Return SECRET_KEY constant used in settings
    """
    file_location = Path(getcwd()+"/security/files/")
    file_to_open = file_location / 'SECRET_KEY'
    
    with open(file_to_open, 'r') as f:
        return f.read()
