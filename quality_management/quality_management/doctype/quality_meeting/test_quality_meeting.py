# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

class TestQualityMeeting(unittest.TestCase):
	
	def test_meeting(self):
		createmeeting = create_meeting()
		print("createmeeting")
		getmeeting = get_meeting()
		print("getmeeting")

def create_meeting():
	meeting = frappe.get_doc({
		"doctype": "Quality Meeting",
		"agenda": "Quality Meeting Test",
		"scope": "Company",
		"date": ""+ frappe.utils.nowdate() +""
	})
	meeting.insert()
	return meeting

def get_meeting():
	meeting = frappe.get_all("Quality Meeting")
	return meeting
