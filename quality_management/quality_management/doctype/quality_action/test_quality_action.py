# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityAction(unittest.TestCase):

	def test_action(self):
		createaction = create_action()
		print("createaction")
		getaction = get_action()
		print("getaction")

def create_action():
	action = frappe.get_doc({
		"doctype": "Quality Action",
		"agenda": "Quality Meeting Test",
		"scope": "Company",
		"date": ""+ frappe.utils.nowdate() +""
	})
	action.insert()
	return action

def get_action():
	action = frappe.get_all("Quality Action")
	return action
