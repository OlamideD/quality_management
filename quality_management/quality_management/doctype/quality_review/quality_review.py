# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QualityReview(Document):	

	def after_insert(self):
		problem = ''
		for value in self.values:
			if int(value.achieved) < int(value.target):
				problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'

		if(problem != ''):
			problem = filter(None, problem.split("\n"))
			doc = frappe.get_doc({
				'doctype': 'Quality Action',
				'action': 'Corrective',
				'type': 'Quality Review',
				'review': ''+ self.name +'',
				'date': ''+ frappe.utils.nowdate() +''
			})
			for data in problem:
				doc.append("description",{
					'problem': data
				})
			doc.insert()
			frappe.db.commit()

	def on_update(self):
		print("On Update")
		problem = ''
		for value in self.values:
			if int(value.achieved) < int(value.target):
				problem = problem + 'In '+ value.objective +', the Achieved Value '+ str(value.achieved) +' is less than the Target Value '+ str(value.target) +'\n'
		print(problem)
		if problem != '':
			problem = filter(None, problem.split("\n"))
			query = frappe.get_list("Quality Action", filters={"review":""+ self.name +""})
			if len(query) == 0:
				doc = frappe.get_doc({
					'doctype': 'Quality Action',
					'action': 'Corrective',
					'type': 'Quality Review',
					'review': ''+ self.name +'',
					'date': ''+ frappe.utils.nowdate() +''
				})
				for data in problem:
					doc.append("description",{
						'problem': data
					})
				doc.insert()
				frappe.db.commit()
			else:
				doc = frappe.delete_doc("Quality Action Table", filters={'parent': ''+ query[0].name +''})
				doc = frappe.get_doc("Quality Action", ""+ query[0].name +"")
				for data in problem:
					doc.append("description",{
						'problem': data
					})
				doc.save
				frappe.db.commit()
		else:
			query = frappe.get_list("Quality Action", filters={"review":""+ self.name +""})
			frappe.delete_doc("Quality Action", ""+ query[0].name +"")