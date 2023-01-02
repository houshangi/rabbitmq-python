class PurchaseOrder:
    def __init__(self, amount_to_pay, po_number, company_name , payment_terms):
        self.amount_to_pay = amount_to_pay
        self.po_number = po_number
        self.compant_name = company_name
        self.payment_terms = payment_terms