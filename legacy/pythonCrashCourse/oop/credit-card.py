class PrivateMethod:
    def __init__(self):
        self.__secretkey = "MY_SOCIAL_SECURITY_NUMBER"

    def __privateMethod(self):
        return "SSN: " + self.__secretKey

    def privateMethod(self):
        return self.__privateMethod()


bankAcc = PrivateMethod()
print(bankAcc.privateMethod())  # => SSN: MY_SOCIAL_SECURITY_NUMBER
# print(bankAcc.__privateMethod())  # fails with function not found...

bankAcc.PrivateMethod
