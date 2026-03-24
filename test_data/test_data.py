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