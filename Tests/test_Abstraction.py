import unittest

from Tutorial.Abstraction import Bank


class MyTestCase(unittest.TestCase):
    def test_instantiate_bank(self):
        bank = Bank()
        self.assertIsInstance(bank, Bank)

    def test_payBills(self):
        bank = Bank()
        string = bank.payBills()
        self.assertEqual(string, "Insufficient balance to pay bills, please make a deposit first")
        bank.deposit(200)
        string = bank.payBills()
        self.assertEqual(string, "Bills paid")


if __name__ == '__main__':
    unittest.main()
