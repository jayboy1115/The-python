import unittest

from pythonProjects.multiples.loan_contract import LoanContract


class TestLoanContract(unittest.TestCase):
    def test_init(self):
        loan_contract = LoanContract("Johnson", 6, 100000, 10)
        self.assertEqual(loan_contract.borrower, "Johnson")
        self.assertEqual(loan_contract.interest_rate, 0.06)
        self.assertEqual(loan_contract.loan_amount, 100000)
        self.assertEqual(loan_contract.loan_period, 10)

    def test_compute_monthly_payment(self):
        loan_contract = LoanContract("Johnson", 6, 100000, 10)
        self.assertAlmostEqual(loan_contract.compute_monthly_payment(), 1117.83, delta = 10)

    def test_compute_total_payment(self):
        loan_contract = LoanContract("Johnson", 6, 100000, 10)
        self.assertAlmostEqual(loan_contract.compute_total_payment(), 133492.07, delta = 267)
