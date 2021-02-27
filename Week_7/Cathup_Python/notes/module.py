def world():
    print('Hello World')

class Greet:
    def __init__(self, name):
        self.name = name
    
    def sayhi(self):
        print(f'Hello {self.name}! How are you? ')

    def saybye(self):
        print(f'Goodbye {self.name}. See you soon!')

