def random_email():
    import random
    import string
    domains = ["example.com", "test.com", "sample.com","saauzi.com"]
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def random_password(length=12):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def random_company_name():
    import random
    import string
    adjectives = ["Tech", "Global", "Innovative", "Dynamic", "Creative"]
    nouns = ["Solutions", "Systems", "Enterprises", "Technologies", "Services"]
    company_name = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
    return f"{company_name} {random.choice(adjectives)} {random.choice(nouns)}"

def random_company_owner():
    import random
    first_names = ["John", "Jane", "Alex", "Emily", "Michael"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

dashboard_contents =["Total Accounts Purchased","Total Accounts Created","Total Accounts Remaining","Total Paid Amount","Total Pending Amount","Active Subscriptions"]
client_summary_contents = ["Total Clients","Total Paid Clients","Today New Clients"]

def client_data():
    import random
    import string
    client_name = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
    client_email = f"{client_name.lower()}@example.com"
    client_phone = ''.join(random.choice(string.digits) for i in range(10))
    return client_name, client_email, client_phone

def random_number_of_subscriptions():
    import random
    return random.randint(10, 999)

def random_remarks():
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def random_ref_id():
    import random
    import string
    return ''.join(random.choice(string.digits) for i in range(10))

def payment_receipt():
    import os
    return os.path.abspath("test_data/payment_receipt.png")

def random_company_website():
    import random
    import string
    domains = ["example.com", "test.com", "sample.com","saauzi.com"]
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    domain = random.choice(domains)
    return f"https://{name}.{domain}"

def random_company_address():
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def random_company_pan():
    import random
    import string
    return ''.join(random.choice(string.digits) for i in range(10))

def random_paragraph(num_sentences=5):
    import random
    sentences = [
        "Innovation drives our success in the modern digital landscape. ",
        "We provide scalable and efficient solutions for all your business needs. ",
        "Our professional team is dedicated to delivering excellence and quality. ",
        "We empower growth through technology and strategic thinking. ",
        "Customer satisfaction is our top priority in every project we undertake. ",
        "Building reliable systems is what characterizes our approach. ",
        "Our journey started with a vision to transform the industry. ",
        "We believe in the power of creative thinking and hard work. ",
        "Transforming challenges into opportunities is our forte. ",
        "Join us as we redefine the boundaries of engineering. "
    ]
    return "".join(random.sample(sentences, min(num_sentences, len(sentences))))

def random_company_details():
    import os
    company_name = random_company_name()
    company_email = f"info@{company_name.lower().replace(' ', '')}.com"
    company_owner = random_company_owner()
    company_phone = random_company_pan()
    company_address = random_company_address()
    company_website = random_company_website()
    company_vat = random_company_pan()
def random_email():
    import random
    import string
    domains = ["example.com", "test.com", "sample.com","saauzi.com"]
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def random_password(length=12):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def random_company_name():
    import random
    import string
    adjectives = ["Tech", "Global", "Innovative", "Dynamic", "Creative"]
    nouns = ["Solutions", "Systems", "Enterprises", "Technologies", "Services"]
    company_name = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
    return f"{company_name} {random.choice(adjectives)} {random.choice(nouns)}"

def random_company_owner():
    import random
    first_names = ["John", "Jane", "Alex", "Emily", "Michael"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

dashboard_contents =["Total Accounts Purchased","Total Accounts Created","Total Accounts Remaining","Total Paid Amount","Total Pending Amount","Active Subscriptions"]
client_summary_contents = ["Total Clients","Total Paid Clients","Today New Clients"]

def client_data():
    import random
    import string
    client_name = ''.join(random.choice(string.ascii_uppercase) for i in range(5))
    client_email = f"{client_name.lower()}@example.com"
    client_phone = ''.join(random.choice(string.digits) for i in range(10))
    return client_name, client_email, client_phone

def random_number_of_subscriptions():
    import random
    return random.randint(10, 999)

def random_remarks():
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def random_ref_id():
    import random
    import string
    return ''.join(random.choice(string.digits) for i in range(10))

def payment_receipt():
    import os
    return os.path.abspath("test_data/payment_receipt.png")

def random_company_website():
    import random
    import string
    domains = ["example.com", "test.com", "sample.com","saauzi.com"]
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    domain = random.choice(domains)
    return f"https://{name}.{domain}"

def random_company_address():
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def random_company_pan():
    import random
    import string
    return ''.join(random.choice(string.digits) for i in range(10))

def random_paragraph(num_sentences=5):
    import random
    sentences = [
        "Innovation drives our success in the modern digital landscape. ",
        "We provide scalable and efficient solutions for all your business needs. ",
        "Our professional team is dedicated to delivering excellence and quality. ",
        "We empower growth through technology and strategic thinking. ",
        "Customer satisfaction is our top priority in every project we undertake. ",
        "Building reliable systems is what characterizes our approach. ",
        "Our journey started with a vision to transform the industry. ",
        "We believe in the power of creative thinking and hard work. ",
        "Transforming challenges into opportunities is our forte. ",
        "Join us as we redefine the boundaries of engineering. "
    ]
    return "".join(random.sample(sentences, min(num_sentences, len(sentences))))

def random_company_details():
    import os
    company_name = random_company_name()
    company_email = f"info@{company_name.lower().replace(' ', '')}.com"
    company_owner = random_company_owner()
    company_phone = random_company_pan()
    company_address = random_company_address()
    company_website = random_company_website()
    company_vat = random_company_pan()

    company_logo = os.path.abspath("test_data/logo.png")
    company_favicon = os.path.abspath("test_data/logo.png")
    
    return company_name, company_email, company_owner, company_phone, company_address, company_website, company_vat, company_logo, company_favicon

def random_unsupported_tld_email():
    import random
    import string
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    return f"{name}@domain.faketld"

# ------------------------------------------------------------------
# NEGATIVE TEST DATA
# ------------------------------------------------------------------

# Signup Negative Data
INVALID_EMAIL_FORMAT = "invalidemail.com"
WHITESPACE_STRING = "     "
SQL_INJECTION_EMAIL_1 = "' OR '1'='1"
XSS_PAYLOAD_SCRIPT = "<script>alert('XSS')</script>"
LONG_STRING = "".join("A" for _ in range(500))
SPECIAL_CHARS_NAME = "!@#$%^&*()_+"

# Login Negative Data
INVALID_EMAIL_NO_AT = "notanemail"
INVALID_EMAIL_NO_DOMAIN = "user@"
WRONG_PASSWORD = "WrongPassword@999"
UNREGISTERED_EMAIL = "ghost.never.registered@example.com"
WRONG_ACCOUNT_EMAIL = "wrong.account@example.com"
SQL_INJECTION_EMAIL_2 = "' OR '1'='1' --"
SQL_INJECTION_PASSWORD = "' OR '1'='1' --"
BOOLEAN_BLIND_SQLI = "admin' AND 1=1--"
