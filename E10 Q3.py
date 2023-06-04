class Account():

  def __init__(self,initial_amount):

    self.balance= initial_amount
    print("Initial amount:",initial_amount)

  def withdraw(self,amount):

    if self.balance>=amount:

      self.balance -= amount

      print("Withdrew:", amount)

    else:

      print(" Insufficient balance ")

  def deposit(self,amount):

    self.balance += amount

    print("Amount Deposited:{}".format(amount))

  def display(self):

    print("Net Available Balance= {}".format(self.balance))

ac = Account(1000)

ac.deposit(2000)

ac.withdraw(1000)

ac.display()
