class IP:
    """
    Models an ip address using OOP:
    Valid ip addresses are in
    the range of 255.255.255.255
    Each of the 4 octets can be within the
    range of 0-255. Write a class in which the user passes
    in valid values in the 4 octets, and
    create a string out it that can be
    viewed in the method create_ip
    """

    def __init__(self, a, b, c, d):
        if 0 <= a <= 255:
            self.a = a
        else:
            raise ValueError("Invalid amount: Enter range 0-255")
        if 0 <= b <= 255:
            self.b = b
        else:
            raise ValueError("Invalid amount: Enter range 0-255")
        if 0 <= c <= 255:
            self.c = c
        else:
            raise ValueError("Invalid amount: Enter range 0-255")
        if 0 <= d <= 255:
            self.d = d
        else:
            raise ValueError("Invalid amount: Enter range 0-255")

    def create_ip(self):
        """
        :return: Builds the ip address
        """
        return f'{self.a}.{self.b}.{self.c}.{self.d}'

    def set_a(self, a):
        """
        :return: The modified value of a
        """
        self.a = a

# print(dir())
# print(__name__)
#

if __name__ == '__main__':
    one = IP(1, 255, 255, 255)
    two = IP(255, 255, 75, 0)
    three = IP(0, 17, 0, 255)
    print(one.create_ip())
    print(two.create_ip())
    print(three.create_ip())
    # four = IP(0, 0, 256, 255)

    # five = IP(-1, 0, 0, 2)
    # six = IP(0, 0, 0, 255.1)


