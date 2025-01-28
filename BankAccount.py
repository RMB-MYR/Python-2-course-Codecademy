class BankAccount():
  balance = 0
  def __init__(self, name):
    self.name = name

  
  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)

  def show_balance(self):
    return "%s $" % (self.balance)


  def deposit(self,amount):
    if amount <= 0:
      print "You have to deposit more than 0$"
      return
    else: 
      print str(amount) + "$ will be added to your account"
      self.balance += amount    
      self.show_balance()

  def withdraw(self, amount):
    if amount >= self.balance:
      print "Error, you can't withdraw that much money $$$"

    else :
      print str(amount) + "$ will be taken out of your account"
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Rembo")
print my_account
print my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(3000)
print my_account


