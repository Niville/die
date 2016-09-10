# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "die_master"
app_title = "Die Master"
app_publisher = "Ragav"
app_description = "Die details"
app_icon = "octicon octicon-database"
app_color = "#202020"
app_email = "sragav95@gmail.com"
app_version = "0.0.1"
app_license = "GNU"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/die_master/css/die_master.css"
# app_include_js = "/assets/die_master/js/die_master.js"

# include js, css files in header of web template
# web_include_css = "/assets/die_master/css/die_master.css"
# web_include_js = "/assets/die_master/js/die_master.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "die_master.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "die_master.install.before_install"
# after_install = "die_master.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "die_master.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"die_master.tasks.all"
# 	],
# 	"daily": [
# 		"die_master.tasks.daily"
# 	],
# 	"hourly": [
# 		"die_master.tasks.hourly"
# 	],
# 	"weekly": [
# 		"die_master.tasks.weekly"
# 	]
# 	"monthly": [
# 		"die_master.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "die_master.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "die_master.event.get_events"
# }

