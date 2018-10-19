# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityReview(unittest.TestCase):

	def test_quality_review(self):
		test_create_review = create_review()
		test_get_review = get_review()
		self.assertEquals(test_create_review.name, test_get_review.name)

def create_review():
	review = frappe.get_doc({
		"doctype": "Quality Review",
		"scope": "Company",
		"date": ""+ frappe.utils.nowdate() +""
	})
	review.insert()
	return review

def get_review():
	review = frappe.get_list("Quality Review")
	return review[0]