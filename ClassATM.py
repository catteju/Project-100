class Atm(object):
    def __init__(self, cardNo, pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def withdrawal(self, amount):
        print("Rs." , amount , " has withdrawan from your account")

    def balanceEnquiry(self):
        print("Balance Not Available")

    def changePin(self, pin):
        print("Your pin number is changed to" , pin)

person1 = Atm(123456, 654321)
person1.withdrawal(2000)
person1.balanceEnquiry()
person1.changePin(456789)