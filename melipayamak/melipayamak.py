from .sms import Rest, Soap
from .branch import Branch
from .users import Users
from .ticket import Ticket
from .contacts import Contacts


class Api:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sms(self, _type="rest"):
        if _type == "rest":
            return Rest(self.username, self.password)
        else:
            return Soap(self.username, self.password)

    def users(self):
        return Users(self.username, self.password)

    def ticket(self):
        return Ticket(self.username, self.password)

    def branch(self):
        return Branch(self.username, self.password)

    def contacts(self):
        return Contacts(self.username, self.password)
