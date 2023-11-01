class Bank_Details:
    def __init__(self, name, account, age, sex):
        self.name = name
        self.account = account
        self.age = age
        self.sex = sex
    def DisplayBank_Details(self):
        print(f" The name is {self.name}")
        print(f" The account is {self.account}")
        print(f" The age is {self.age}")
        print(f" The sex is {self.sex}")

Bank_Details1 = Bank_Details("lawrence", "1505991956", "19", "male")

Bank_Details1.DisplayBank_Details()

