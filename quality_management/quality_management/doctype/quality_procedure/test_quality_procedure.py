# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityProcedure(unittest.TestCase):
	
	def test_procedure(self):
		createprocedure = create_procedure()
		print("createprocedure")
		getprocedure = get_procedure()
		print("getprocedure")

def create_procedure():
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

def get_procedure():
	procedure = frappe.get_all("Quality Procedure")
	return procedure
