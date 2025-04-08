# TODO:

class BankAccount:
	def __init__(self, owner): # __init__ = constructor, self = ref to the object, owner = param/variable
		self.owner = owner
		self.balance = 0
		self.history = []
	
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.history.append(f"Deposited {amount}")
			print(f"Deposited {amount}. New balance: {self.balance}")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		if (amount <= self.balance):
			self.balance -= amount
			self.history.append(f"Withdrawed {amount}")
			print(f"Withdrawed {amount}. New balance: {self.balance}")
		else:
			print("Withdraw amount must be inferior to account balance")
	
	def show_balance(self):
		print(f"Balance: {self.balance}")

	def display_history(self):
		print(f"Transaction history: {self.history}")

def main():
	account = BankAccount("John")
	account.show_balance()
	account.display_history()
	account.deposit(10)
	account.deposit(-2)
	account.withdraw(20)
	account.withdraw(10)
	account.deposit(50)
	account.show_balance()
	account.display_history()

if __name__ == "__main__": # if run directly = "__main__", else it's an imported module in another file == module name
	main()
