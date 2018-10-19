# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityProcedure(unittest.TestCase):
	
	def test_quality_procedure(self):		
		test_create_procedure = create_procedure()
		test_get_procedure = get_procedure()
		self.assertEquals(test_create_procedure.name, test_get_procedure.name)

"""		test_create_goal = create_goal()
		test_get_goal = get_goal()
		self.assertEquals(test_create_goal.name, test_get_goal.name)
		
		test_create_unit = create_unit()
		test_get_unit = get_unit()
		self.assertEquals(test_create_unit.name, test_get_unit.name)

		test_create_review = create_review()
		test_get_review = get_review()
		self.assertEquals(test_create_review.name, test_get_review.name)
		
		test_action = get_action()
		self.assertEquals(test_action.review, test_create_review.name)
		
		test_create_meeting = create_meeting()
		test_get_meeting = get_meeting()
		self.assertEquals(test_create_meeting.name, test_get_meeting.name)

		test_create_feedback = create_feedback()
		test_get_feedback = get_feedback()
		self.assertEquals(test_create_feedback.name, test_get_feedback.name)

		test_create_template = create_template()
		test_get_template = get_template()
		self.assertEquals(test_get_template.name, test_create_template.name)"""

def create_procedure():
	procedure = frappe.get_doc({
		"doctype": "Quality Procedure",
		"procedure": "_Test Quality Procedure",
		"procedure_step": [
			{
				"step": "_Test Quality Procedure Table",
			}
		]
	})
	procedure.insert()
	return procedure

def get_procedure():
	procedure = frappe.get_list("Quality Procedure")
	return procedure[0]
"""
def create_goal():
	goal = frappe.get_doc({
		"doctype": "Quality Goal",
		"goal": "Quality Goal Test",
		"revision": "1",
		"frequency": "Daily",
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
	goal = frappe.get_list("Quality Goal")
	return goal[0]

def create_unit():
	unit = frappe.get_doc({
		"doctype": "Measurement Unit",
		"unit": "Test Unit"
	})
	unit.insert()
	return unit

def get_unit():
	unit = frappe.get_list("Measurement Unit")
	return unit[0]

def create_review():
	for data in frappe.get_all("Quality Goal",fields=['name','frequency']):
		if data.frequency == 'None':
			objectives = frappe.get_all("Quality Objective", filters={'parent': ''+ data.name +''}, fields=['objective', 'target', 'unit'])
			review = frappe.get_doc({
				"doctype": "Quality Review",
				"goal": data.name,
				"date": ""+ frappe.utils.nowdate() +"",
			})
			for objective in objectives:
				review.append("values",{
					'objective': objective.objective,
					'target': objective.target,
					'target_unit': objective.unit,
					'achieved': "2",
					'achieved_unit': objective.unit
				})
			review.insert()
			return review

def get_review():
	review = frappe.get_list("Quality Review")
	return review[0]

def get_action():
	action = frappe.get_list("Quality Action", fields=["name","review"])
	return action[0]

def create_meeting():
	meeting = frappe.get_doc({
		"doctype": "Quality Meeting",
		"scope": "Company",
		"status": "Close",
		"date": ""+ frappe.utils.nowdate() +""
	})
	meeting.insert()
	return meeting

def get_meeting():
	meeting = frappe.get_list("Quality Meeting", fields=['name', 'status'])
	return meeting[0]

def create_feedback():
	feedback = frappe.get_doc({
		"doctype": "Customer Feedback",
		"date": ""+ frappe.utils.nowdate() +""
	})
	feedback.insert()
	return feedback

def get_feedback():
	feedback = frappe.get_list("Customer Feedback", fields=['name', 'date'])
	return feedback[0]

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
	template = frappe.get_list("Customer Feedback Template", fields=['name', 'template'])
	return template[0]
"""