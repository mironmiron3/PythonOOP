class BankAccount:
    def __init__(self, credit_card, phone, address):
        self.credit_card = credit_card
        self.phone = phone
        self.address = address




class CreditCard:
    def __init__(self, number, cvv):
        self.number = number
        self.__cvv = cvv

my_credit_card = CreditCard(5588, 123)
my_bank_account = BankAccount(my_credit_card, 867439853, "Sofia")

print(my_bank_account.credit_card)
