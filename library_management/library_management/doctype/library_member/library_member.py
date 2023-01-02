# Copyright (c) 2022, labeeb and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
class LibraryMember(WebsiteGenerator):
	pass
class LibraryMember(Document):
    #this method will run every time a document is saved
	  def before_save(self):
                      self.full_name = f'{self.first_name} {self.last_name or ""}'
					  
	
