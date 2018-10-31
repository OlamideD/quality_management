# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_dependencies = ["Quality Procedure","Measurement Unit" ,"Quality Goal", "Quality Review"]

class TestQualityAction(unittest.TestCase):

	def test_quality_action(self):
		test_create_action = create_action()
		test_get_action = get_action()
		self.assertEquals(test_create_action.name, test_get_action.name)

def create_action():
	action = frappe.get_doc({
		#add here
	})
	action_exist = frappe.get_list("Quality Action", filters={"goal": "_Test Quality Goal"})
	if len(action_exist) == 0:
		action.insert()
		return action
	else:
		return action_exist[0]

def get_action():
	action = frappe.get_list("Quality Action")
	return action[0]