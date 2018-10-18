# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestFeedbackTemplate(unittest.TestCase):

	def test_template(self):
		createtemplate = create_template()
		print("createtemplate")
		gettemplate = get_template()
		print("gettemplate")

def create_template():
	template = frappe.get_doc({
		"doctype": "Feedback Template",
		"template": "Template Test",
		"scope": "Company",
		"feedback": [
			{
				"feedback_parameter": "Feedback Template",
			}
		]
	})
	template.insert()
	return template

def get_template():
	template = frappe.get_all("Quality Template")
	return template
