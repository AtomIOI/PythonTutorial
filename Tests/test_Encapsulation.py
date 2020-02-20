import unittest

from Tutorial.Encapsulation import Bank


class MyTestCase(unittest.TestCase):

    def test_instantiate_bank(self):
        bank = Bank()
        self.assertIsInstance(bank, Bank)

    def test_check_balance(self):
        bank = Bank()
        self.assertEqual(0, bank.checkBalance())

    def test_deposit(self):
        bank = Bank()
        bank.deposit(100)
        self.assertEqual(100, bank.checkBalance())

    def test_withdraw(self):
        bank = Bank()
        bank.withdraw(100)
        self.assertEqual(0, bank.checkBalance())
        bank.deposit(200)
        bank.withdraw(100)
        self.assertEqual(100, bank.checkBalance())


if __name__ == '__main__':
    unittest.main()
