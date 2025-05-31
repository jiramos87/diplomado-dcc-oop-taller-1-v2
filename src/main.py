from accounts import CurrentAccount, CheckingAccount, StudentAccount

# instantiate one object from CurrentAccount and one object from CheckingAccount and make some deposits, withdrawals and transfers between them.
# Make sure to handle the cases where the balance is not enough to withdraw the amount or the target account is not a CheckingAccount.

if __name__ == "__main__":
    current_account = CurrentAccount()
    checking_account = CheckingAccount()
    student_account = StudentAccount()
    
    current_account.deposit(1000)
    checking_account.deposit(1000)
    student_account.deposit(1000)

    current_account.withdraw(500)
    checking_account.withdraw(500)
    student_account.withdraw(500)

    current_account.transfer(200, checking_account)
    checking_account.transfer(200, student_account)
    student_account.transfer(200, current_account)

    print(current_account.balance)
    print(checking_account.balance)
    print(student_account.balance)

    print(current_account.transfer(1000000, checking_account))
    print(checking_account.transfer(1000000, student_account))
    print(student_account.transfer(1000000, current_account))

    print(current_account.transfer(1000000, checking_account))
    print(checking_account.transfer(1000000, student_account))
    print(student_account.transfer(1000000, current_account))
