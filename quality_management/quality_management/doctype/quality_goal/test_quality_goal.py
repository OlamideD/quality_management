# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityGoal(unittest.TestCase):
	
	def test_quality_goal(self):
		test_create_goal = create_goal()
		test_get_goal = get_goal()
		self.assertEquals(test_create_goal.name, test_get_goal.name)

def create_goal():
	goal = frappe.get_doc({
		"doctype": "Quality Goal",
		"goal": "Quality Goal Test",
		"revision": "1",
		"frequency": "Daily",
		"objective": [
			{
				"objective": "Test Quality Objective",
				"target": "4",
			}
		]
	})
	goal.insert()
	return goal

@frappe.whitelist()
def get_goal():
	goal = frappe.get_list("Quality Goal")
	return goal[0]