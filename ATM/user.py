import json
import os


DATA_FILE = "C:/PYTHON/ATM/users.json"

def load_users(path=DATA_FILE):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
print(load_users())