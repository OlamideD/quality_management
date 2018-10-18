# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityMeeting(unittest.TestCase):
	pass

#	def unit_test(self):
#		test_create_meeting = create_meeting()
#		test_get_meeting = get_meeting()
#		self.assertEquals(test_create_meeting.name, test_get_meeting.name)

#def create_meeting():
#	meeting = frappe.get_doc({
#		"doctype": "Quality Meeting",
#		"scope": "Company",
#		"status": "Close",
#		"date": ""+ frappe.utils.nowdate() +""
#	})
#	meeting.insert()
#	return meeting

#def get_meeting():
#	meeting = frappe.get_list("Quality Meeting", fields=['name', 'status'])
#	return meeting[0]