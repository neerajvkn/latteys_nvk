from __future__ import unicode_literals
from frappe import _
import frappe
import datetime

def send_at_set_time():
	now = datetime.datetime.now()	
	timestamp = now.strftime('%H'+'.00')
	enabled_reports = frappe.get_all('Auto Email Report',
		filters={'ls_enabled': 1, 'frequency': 'At Set Time'})

	for report in enabled_reports:
		# print(report)
		auto_email_report = frappe.get_doc('Auto Email Report', report.name)
		# if not set to send at current hour, skip
		if auto_email_report.ls_send_at_hour != timestamp:
			print(str(report) + " not in time slot" )
			continue
		try:
			auto_email_report.send()
		except Exception as e:
			frappe.log_error(e, _('Failed to send {0} Auto Email Report').format(auto_email_report.name))