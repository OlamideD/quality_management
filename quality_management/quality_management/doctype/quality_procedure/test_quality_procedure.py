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