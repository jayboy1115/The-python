class LoanContract:
    def __init__(self, borrower, interest_rate, loan_amount, loan_period):
        self.borrower = borrower
        self.interest_rate = interest_rate / 100
        self.loan_amount = loan_amount
        self.loan_period = loan_period

    def compute_monthly_payment(self):
        monthly_interest_rate = self.interest_rate / 12
        number_of_payments = self.loan_period * 12
        monthly_payment = (self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / (
                (1 + monthly_interest_rate) ** number_of_payments - 1)
        return round(monthly_payment, 2)

    def compute_total_payment(self):
        monthly_payment = self.compute_monthly_payment()
        total_payment = monthly_payment * self.loan_period * 12
        return round(total_payment, 2)
