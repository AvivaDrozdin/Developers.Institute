# class Dog():
#     def __init__(self, name, age, weight, breed):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.breed = breed


#     def mate(self, other_dog):
#         new_pup_name = self.name + other_dog.name
#         new_pup_breed = self.breed + other_dog.breed

#         return Dog(new_pup_name, 0.1, 1, new_pup_breed)


#     def bark(self):
#         return print('Bark Bark Bark')


#     def run_speed(self):
#         return (self.weight/self.age)*10


#     def fight(self, other_dog):
#         self_score = self.run_speed() * self.weight
#         other_score =  other_dog.run_speed() * other_dog.weight
        
#         winner = None
#         if self_score > other_score:
#             winner = self
#         elif self_score < other_score:
#             winner = other_dog

#         if winner:
#             print(f'{winner.name} wins!')
#         else:
#             print('Draw!')

# d1 = Dog('Rex', 6, 45, 'Pitbul')
# d2 = Dog('Fifi', 5, 20, 'Labrador')



#Trial 2 
#make class bank with acc nr & balance
#withdraw money
#add money
#check balance
#print transaction history

class Bank:
    def __init__(self, acc_nr, balance=0):
        self.acc = acc_nr
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        if amount <= 0:
            print('Invalid amount')
        self.history.append(f'Deposited: {amount}')


    def withdraw(self, amount):
        if amount >= self.balance:
            print ("You don't have that much money, go back to work")
        else:
            self.balance -= amount
        self.history.append(f'Withdraw: {amount}')
        return amount

    def check_balance(self):
        print(self.balance)

    def transaction_history(self):
        for each_item in self.history:
            print(each_item)















# class Bank:
#     def __init__(self, account_nr, pin, balance = 0 ):
#         self.account_nr = account_nr
#         self.pin = pin
#         self.balance = balance
#         self.history = []
    
#     def deposit(self, amount):
#         self.balance += amount
#         self.history.append(f'Deposit: {amount}')


#     def withdraw(self, amount):
#         if amount >= self.balance:
#             print ("You don't have that much money, go back to work")
#         else:
#             self.balance -= amount

#         self.history.append(f'Withdraw: {amount}')
        
#         return amount
        

#     def show_balance(self):
#         print(self.balance)


#     def show_history(self):
#         for item in self.history:
#             print(item)
    

        

