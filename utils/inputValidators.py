import re
from termcolor import colored

def validateEmail(email):
    email_pattern = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    if email_pattern.match(email):
        return True
    else:
        return False
    
def validateProxy(proxy):
    parts = proxy.split(':')
    if len(parts) != 4:
        raise ValueError("Proxy string format must be ip:port:user:pass")

    ip, port, user, password = parts

    return [ip, port, user, password]