import random

def decToHex(dec, bits):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 
                        4: '4', 5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 
                        12: 'C', 13: 'D', 14: 'E', 15: 'F'} 
    hexadecimal = []
    while dec > 0: 
        remainder = dec % 16
        hexadecimal = [conversion_table[remainder]] + hexadecimal
        dec = dec // 16
    
    while len(hexadecimal) * 4 < bits:
        hexadecimal = ['0'] + hexadecimal

    return ''.join(hexadecimal)


class DNSMessage:
    def __init__(self, hostname):
        self.header = Header()
        self.question = Question(hostname)


class Header:
    def __init__(self):
        self.id = decToHex(self.generateID(), 16)
        self.flags = "0100"
        self.qdcount = decToHex(1, 16)
        self.ancount = self.nscount = self.arcount = decToHex(0, 16)
    
    def generateID(self) -> int:
        id = random.randint(0, 255)
        return id


# class Question:
#     def __init__(self, hostname):
#         self.qname = self.encode(hostname)

#     def encode(self, hostname):
#         hostname = hostname.split('.')
#         res = []

#         for label in hostname:
#             res.append(f'{len(label)}{label}')
#         res.append('0')
        
#         return ''.join(res)

