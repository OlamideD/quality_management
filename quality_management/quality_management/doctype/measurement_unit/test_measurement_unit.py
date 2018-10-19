# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestMeasurementUnit(unittest.TestCase):

	def test_measurement_unit(self):
		test_create_unit = create_unit()
		test_get_unit = get_unit()
		self.assertEquals(test_create_unit.name, test_get_unit.name)

def create_unit():
	unit = frappe.get_doc({
		"doctype": "Measurement Unit",
		"unit": "_Test Unit"
	})
	unit.insert()
	return unit

def get_unit():
	unit = frappe.get_list("Measurement Unit")
	return unit[0]