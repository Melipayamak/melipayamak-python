from .sms import Rest, Soap, RestAsync, SoapAsync
from .branch import Branch
from .branchAsync import BranchAsync
from .users import Users
from .usersAsync import UsersAsync
from .ticket import Ticket
from .ticketAsync import TicketAsync
from .contacts import Contacts
from .contactsAsync import ContactsAsync


class Api:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sms(self, _method="rest", _type=""):
        if _method == "rest":
            if _type == "async":
                return RestAsync(self.username, self.password)
            else:
                return Rest(self.username, self.password)
        else:
            if _type == "async":
                return SoapAsync(self.username, self.password)
            else:
                return Soap(self.username, self.password)

    def users(self):
        return Users(self.username, self.password)

    def usersAsync(self):
        return UsersAsync(self.username, self.password)

    def ticket(self):
        return Ticket(self.username, self.password)

    def ticketAsync(self):
        return TicketAsync(self.username, self.password)

    def branch(self):
        return Branch(self.username, self.password)

    def branchAsync(self):
        return BranchAsync(self.username, self.password)

    def contacts(self):
        return Contacts(self.username, self.password)

    def contactsAsync(self):
        return ContactsAsync(self.username, self.password)
