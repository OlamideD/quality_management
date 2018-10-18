# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityGoal(unittest.TestCase):
	
	def test_goal(self):
		creategoal = create_goal()
		print("creategoal")
		getgoal = get_goal()
		print("getgoal")

def create_goal():
	goal = frappe.get_doc({
		"doctype": "Quality Goal",
		"goal": "Quality Goal Test",
		"revision": "1",
		"frequency": "None",
		"objective": [
			{
				"objective": "Test Quality Goal 4",
				"target": "4",
			}
		]
	})
	goal.insert()
	return goal

def get_goal():
	goal = frappe.get_all("Quality Goal")
	return goal
