import random
import datetime
import os

class BankAccount:
    # Class variable to keep track of account numbers
    _account_counter = 1000
    
    def __init__(self, username, accountType, balance=0):
        """
        Constructor for creating a bank account
        Args:
            username (str): Name of the account holder
            accountType (str): Type of account ('checking' or 'saving')
            balance (float): Initial balance (default: 0)
        """
        # Validate account type
        if accountType.lower() not in ['checking', 'saving']:
            raise ValueError("Account type must be 'checking' or 'saving'")
        
        # Initialize account properties
        self.username = username
        self.accountType = accountType.lower()
        self.balance = float(balance)
        
        # Generate unique account ID
        BankAccount._account_counter += 1
        self.account_id = BankAccount._account_counter
        
        # Create statement file
        self._create_statement_file()
        
        # Log account creation
        self._log_transaction("ACCOUNT_CREATED", 0, f"Account created with initial balance: ${self.balance:.2f}")
    
    def _create_statement_file(self):
        """Create a statement file for the user following the naming format"""
        # File naming format: username_accountType_userID.txt
        self.statement_filename = f"{self.username}_{self.accountType}_{self.account_id}.txt"
        
        # Create the file with header information
        with open(self.statement_filename, 'w') as file:
            file.write("="*60 + "\n")
            file.write(f"BANK ACCOUNT STATEMENT\n")
            file.write("="*60 + "\n")
            file.write(f"Account Holder: {self.username}\n")
            file.write(f"Account Type: {self.accountType.title()}\n")
            file.write(f"Account ID: {self.account_id}\n")
            file.write(f"Statement Created: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*60 + "\n")
            file.write("TRANSACTION HISTORY:\n")
            file.write("-"*60 + "\n")
    
    def _log_transaction(self, transaction_type, amount, description=""):
        """Log a transaction to the statement file"""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(self.statement_filename, 'a') as file:
            file.write(f"{timestamp} | {transaction_type:<12} | ${amount:>8.2f} | Balance: ${self.balance:>8.2f} | {description}\n")
    
    def deposit(self, amount):
        """
        Deposit money into the account
        Args:
            amount (float): Amount to deposit
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return False
        
        self.balance += amount
        self._log_transaction("DEPOSIT", amount, f"Deposited ${amount:.2f}")
        print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the account
        Args:
            amount (float): Amount to withdraw
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient funds! Available balance: ${self.balance:.2f}")
            self._log_transaction("WITHDRAWAL_FAILED", amount, f"Failed withdrawal attempt - Insufficient funds")
            return False
        
        self.balance -= amount
        self._log_transaction("WITHDRAWAL", amount, f"Withdrew ${amount:.2f}")
        print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def get_balance(self):
        """
        Get the current account balance
        Returns:
            float: Current balance
        """
        return self.balance
    
    def get_user_id(self):
        """
        Get the user's account ID
        Returns:
            int: Account ID
        """
        return self.account_id
    
    def get_username(self):
        """
        Get the username
        Returns:
            str: Username
        """
        return self.username
    
    def get_account_type(self):
        """
        Get the account type
        Returns:
            str: Account type
        """
        return self.accountType
    
    def get_transaction_history(self):
        """
        Get transaction history by reading the statement file
        Returns:
            str: Contents of the statement file
        """
        try:
            with open(self.statement_filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Error: Statement file not found!"
    
    def print_account_info(self):
        """Print account information summary"""
        print(f"\n{'='*50}")
        print(f"ACCOUNT INFORMATION")
        print(f"{'='*50}")
        print(f"Account Holder: {self.username}")
        print(f"Account Type: {self.accountType.title()}")
        print(f"Account ID: {self.account_id}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Statement File: {self.statement_filename}")
        print(f"{'='*50}\n")


def test_bank_account_system():
    """Test the bank account system with multiple objects and transactions"""
    print("🏦 BANK ACCOUNT SYSTEM TEST 🏦\n")
    
    # Test 1: Create multiple accounts
    print("📝 Creating multiple bank accounts...")
    
    # Account 1: Checking account
    account1 = BankAccount("John_Doe", "checking", 1000)
    account1.print_account_info()
    
    # Account 2: Savings account
    account2 = BankAccount("Jane_Smith", "saving", 500)
    account2.print_account_info()
    
    # Account 3: Checking account with zero balance
    account3 = BankAccount("Bob_Johnson", "checking")
    account3.print_account_info()
    
    # Test 2: Perform various transactions
    print("💰 Performing transactions...\n")
    
    # Account 1 transactions
    print("--- John Doe's Transactions ---")
    account1.deposit(250)
    account1.withdraw(150)
    account1.withdraw(2000)  # Should fail - insufficient funds
    account1.deposit(75)
    print(f"Final balance: ${account1.get_balance():.2f}\n")
    
    # Account 2 transactions
    print("--- Jane Smith's Transactions ---")
    account2.withdraw(100)
    account2.deposit(300)
    account2.withdraw(150)
    print(f"Final balance: ${account2.get_balance():.2f}\n")
    
    # Account 3 transactions
    print("--- Bob Johnson's Transactions ---")
    account3.withdraw(50)   # Should fail - insufficient funds
    account3.deposit(200)
    account3.withdraw(75)
    account3.deposit(25)
    print(f"Final balance: ${account3.get_balance():.2f}\n")
    
    # Test 3: Display account information
    print("📊 Account Information Summary:")
    accounts = [account1, account2, account3]
    
    for account in accounts:
        print(f"User: {account.get_username()}")
        print(f"ID: {account.get_user_id()}")
        print(f"Type: {account.get_account_type()}")
        print(f"Balance: ${account.get_balance():.2f}")
        print("-" * 30)
    
    # Test 4: Display transaction history for one account
    print("\n📜 Transaction History for John Doe:")
    print(account1.get_transaction_history())
    
    # Test 5: List created statement files
    print("\n📁 Created Statement Files:")
    for account in accounts:
        if os.path.exists(account.statement_filename):
            print(f"✅ {account.statement_filename}")
        else:
            print(f"❌ {account.statement_filename} (not found)")


# Main execution
if __name__ == "__main__":
    test_bank_account_system()