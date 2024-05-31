import toml
import os
import hashlib

path = os.getcwd() + "\\config.toml"
def get_login_info():
    config = toml.load(path)
    password = config['account']['password']
    try:
        if config['account']['password_hash'] == "False":
            hash_password = hashlib.sha256(password.encode()).hexdigest()
            return hash_password
    except KeyError:
        return password
    
def set_account_password(password):
    config = toml.load(path)
    config['account']['password'] = password
    config['account']['password_hash'] = "True"
    with open(path, 'w') as f:
        toml.dump(config, f)
    return