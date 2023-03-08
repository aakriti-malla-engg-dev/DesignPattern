class Address:
    def __init__(self, zipNo, street):
        self.zipNo = zipNo
        self.street = street


class User:
    def __init__(self, name):
        self.name = name


class UserBuilder:
    def __init__(self, name):
        self.user = User(name)

    def setAge(self, age):
        self.user.age = age
        return self

    def setPhone(self, phone):
        self.user.phone = phone
        return self

    def setAddress(self, address):
        self.user.address = address
        return self

    def build(self):
        return self.user


address = Address('12345', 'Main St.')
builder = UserBuilder('Bob').setAge(30).setPhone('765586886').setAddress(address).build()
print(builder.name, builder.age, builder.phone,builder.address.zipNo,builder.address.street )
