import string
import random

def generate_username_email(user_prefix=None,domain=None):
    if not user_prefix:
        user_prefix="testUser"
    if not domain:
        domain="testProject.com"

    username="".join(random.choices(string.ascii_lowercase,k=5))
    email="".join(random.choices(string.ascii_lowercase,k=5))
    username_new=user_prefix+"_"+username
    email_new=email+"@"+domain
    generate={
        "new_username":username_new,
        "new_email":email_new

    }
    return generate


