# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestPerformanceMonitoring(unittest.TestCase):
	
	def test_review(self):
		createreview = create_review_withaction()
		print("createreview")

def create_review_withaction():
	for data in frappe.get_all("Quality Goal",fields=['name','frequency']):
		if data.frequency == 'None':
			print(data.frequency)
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