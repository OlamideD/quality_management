# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestMeasurementUnit(unittest.TestCase):
	
	def test_unit(self):
		createunit = create_unit()
		print("createunit")

def create_unit():
	unit = frappe.get_doc({
		"doctype": "Measurement Unit",
		"unit": "Test Unit"
	})
	unit.insert()
	return unit