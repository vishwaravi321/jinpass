# Copyright (c) 2024, Mr.Jindoblu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Passwords(Document):
	pass



@frappe.whitelist(allow_guest=True)
def get_all_passwords():
	data = frappe.get_all('Passwords')
	return data 

