# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestCustomerFeedbackTemplate(unittest.TestCase):
	
	def test_customer_feedback_template(self):
		test_create_template = create_template()
		test_get_template = get_template()
		self.assertEquals(test_get_template.name, test_create_template.name)

def create_template():
	template = frappe.get_doc({
		"doctype": "Customer Feedback Template",
		"template": "Template Test",
		"scope": "Company",
		"feedback_parameter": [
			{
				"parameter": "Test Feedback Template",
			}
		]
	})
	template.insert()
	return template

def get_template():
	template = frappe.get_list("Customer Feedback Template")
	return template[0]