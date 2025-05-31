import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from accounts import CurrentAccount, CheckingAccount, StudentAccount

class TestAccounts(unittest.TestCase):
    def test_current_account(self):
        current_account = CurrentAccount()
        target_account = CheckingAccount()
        
        self.assertEqual(current_account.balance, 0)
        self.assertTrue(current_account.deposit(1000))
        self.assertEqual(current_account.balance, 1000)
        self.assertTrue(current_account.withdraw(500))
        self.assertEqual(current_account.balance, 500)
        self.assertTrue(current_account.transfer(200, target_account))
        self.assertEqual(current_account.balance, 300)
        self.assertEqual(target_account.balance, 200)

    def test_checking_account(self):
        checking_account = CheckingAccount()
        target_account = StudentAccount()
        
        self.assertEqual(checking_account.balance, 0)
        self.assertTrue(checking_account.deposit(1000))
        self.assertEqual(checking_account.balance, 1000)
        self.assertTrue(checking_account.withdraw(500))
        self.assertEqual(checking_account.balance, 500)
        self.assertTrue(checking_account.transfer(200, target_account))
        self.assertEqual(checking_account.balance, 300)
        self.assertEqual(target_account.balance, 200)  # Use target_account, not StudentAccount()

    def test_student_account(self):
        student_account = StudentAccount()
        target_account = CurrentAccount()  # Create target instance
        
        self.assertEqual(student_account.balance, 0)
        self.assertTrue(student_account.deposit(1000))
        self.assertEqual(student_account.balance, 1000)
        self.assertTrue(student_account.withdraw(500))
        self.assertEqual(student_account.balance, 500)
        self.assertTrue(student_account.transfer(200, target_account))
        self.assertEqual(student_account.balance, 300)
        self.assertEqual(target_account.balance, 200)  # Use target_account, not CurrentAccount()

# test the student account providing different parameters
    def test_student_account_with_different_parameters(self):
        student_account = StudentAccount(max_money=10000, max_deposit=10000, max_transfer=1000)
        target_account = CurrentAccount()

        self.assertEqual(student_account.balance, 0)
        self.assertTrue(student_account.deposit(10000))
        self.assertEqual(student_account.balance, 10000)

        self.assertFalse(student_account.deposit(10001))
        self.assertEqual(student_account.balance, 10000)

        self.assertTrue(student_account.withdraw(5000))
        self.assertEqual(student_account.balance, 5000)

        self.assertFalse(student_account.withdraw(5001))
        self.assertEqual(student_account.balance, 5000)

if __name__ == "__main__":
    unittest.main()