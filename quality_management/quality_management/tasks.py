from __future__ import unicode_literals
import frappe
import datetime
from frappe.utils import date_diff, nowdate, formatdate, add_days

def review():
	now = datetime.datetime.now()
	day = now.day
	day_name = now.strftime("%A")
	month=now.strftime("%B")

	for data in frappe.get_all("Quality Goal",fields=['name', 'frequency', 'date', 'weekly', 'non_measurable']):
		if data.frequency == 'Daily':
			create_review(data.name, data.non_measurable)

		elif data.frequency == 'Weekly':
			if data.weekly == day_name:
				create_review(data.name, data.non_measurable)

		elif data.frequency == 'Monthly':
			if data.date == str(day):
				create_review(data.name, data.non_measurable)


		elif data.frequency == 'Quarterly':
			if (month == 'January' or month == 'April' or month == 'July' or month == 'October') and str(day) == data.date:
				create_review(data.name, data.non_measurable)

		elif data.frequency == 'Half Yearly':
			if (month == 'January' or month == 'July') and str(day) == data.date:
				create_review(data.name, data.non_measurable)

		elif data.frequency == 'Yearly':
			if month == data.yearly and str(day) == data.date:
				create_review(data.name, data.non_measurable)

		elif data.frequency == 'None':
			pass

def create_review(name, non_measurable):
	objectives = frappe.get_all("Quality Objective", filters={'parent': ''+ name +''}, fields=['objective', 'target', 'unit'])
	doc = frappe.get_doc({
		"doctype": "Quality Review",
   		"goal": name,
   		"date": frappe.utils.nowdate(),
		"non_measurable": non_measurable,
	})
	for objective in objectives:
		doc.append("values",{
			'objective': objective.objective,
			'target': objective.target,
			'unit': objective.unit
		})
	doc.insert()
	frappe.db.commit()