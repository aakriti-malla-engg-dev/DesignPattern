class Address:
    def __init__(self, zipNo, street):
        self.zipNo = zipNo
        self.street = street


class User:
    def __init__(self, name, age=None, phone=1279127971, address=None):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address


user = User('Bob', age=10, phone=4884377, address=Address('11', 'Main'))
print(user.name, user.age, user.phone, user.address.zipNo, user.address.street)
