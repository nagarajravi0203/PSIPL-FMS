import frappe
from frappe.model.document import Document

class PSIPLFMSItem(Document):
    def validate(self):
        if self.qty and self.qty <= 0:
            frappe.throw("Quantity must be > 0")
