# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityProcedure(unittest.TestCase):
	
	def test_quality_management(self):
		test_procedure = procedure()
		test_goal = goal()
		test_unit = unit()

		#test_create_review = create_review()
		#test_get_review = get_review()
		
		#test_action = get_action()
		
		#test_meeting = meeting()
		#test_template = template()
		#test_feedback = feedback()

		print(test_procedure.name)
		#self.assertEquals(test_procedure[0].name, 'Quality Procedure Test')
		print(test_goal.name)
		#self.assertEquals(test_goal[0].name, 'Quality Goal Test')
		print(test_unit.name)
		#self.assertEquals(test_unit[0].name, 'Unit Test')
		#self.assertEquals(test_review[0].name)
		#self.assertEquals(test_action[0].name)
		#self.assertEquals(test_meeting[0].name)
		#self.assertEquals(test_template[0].name)
		#self.assertEquals(test_feedback[0].name)

def procedure():
	procedure = frappe.get_doc({
		"doctype": "Quality Procedure",
		"procedure": "Quality Procedure Test",
		"procedure_step": [
			{
				"step": "Test Quality Proceure Step",
			}
		]
	})
	procedure.insert()
	return procedure

def goal():
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

def unit():
	unit = frappe.get_doc({
		"doctype": "Measurement Unit",
		"unit": "Test Unit"
	})
	unit.insert()
	return unit

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

def get_action():
	action = frappe.get_doc({
		"doctype": "Quality Action",
		"agenda": "Quality Meeting Test",
		"scope": "Company",
		"date": ""+ frappe.utils.nowdate() +""
	})
	action.insert()
	return action

def meeting():
	meeting = frappe.get_doc({
		"doctype": "Quality Meeting",
		"scope": "Company",
		"date": ""+ frappe.utils.nowdate() +""
	})
	meeting.insert()
	return meeting

def template():
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

def feedback():
	feedback = frappe.get_doc({
		"doctype": "Customer Feedback",
		"date": ""+ frappe.utils.nowdate() +""
	})
	feedback.insert()
	return feedback