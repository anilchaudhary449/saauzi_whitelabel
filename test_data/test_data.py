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
