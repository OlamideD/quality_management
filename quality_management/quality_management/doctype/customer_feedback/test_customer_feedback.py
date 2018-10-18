# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestCustomerSurvey(unittest.TestCase):

	def test_feedback(self):
		createfeedback = create_feedback()
		print("createfeedback")
		getfeedback = get_feedback()
		print("getfeedback")

def create_feedback():
	feedback = frappe.get_doc({
		"doctype": "Customer Feedback",
		"date": ""+ frappe.utils.nowdate() +""
	})
	feedback.insert()
	return feedback

def get_feedback():
	feedback = frappe.get_all("Customer Feedback")
	return feedback
