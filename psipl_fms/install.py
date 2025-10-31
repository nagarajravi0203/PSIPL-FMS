import frappe

def after_install():
    # create Module Def if not exists
    if not frappe.db.exists("Module Def", "PSIPL FMS"):
        frappe.get_doc({"doctype":"Module Def", "module_name":"PSIPL FMS", "app_name":"psipl_fms"}).insert(ignore_permissions=True)
        frappe.db.commit()
        
    create_contact_submission_webform()

def create_contact_submission_webform():
    """Create the Contact Submission Web Form if not exists"""
    if not frappe.db.exists("Web Form", "contact-submission"):
        webform = frappe.get_doc({
            "doctype": "Web Form",
            "title": "Contact Submission",
            "route": "contact-submission",
            "module": "PSIPL FMS",
            "doctype_name": "Contact Submission",
            "published": 1,
            "is_standard": 1,
            "web_form_fields": [
                {
                    "fieldname": "full_name",
                    "label": "Full Name",
                    "fieldtype": "Data",
                    "reqd": 1,
                    "show_in_list": 1
                },
                {
                    "fieldname": "email",
                    "label": "Email",
                    "fieldtype": "Data",
                    "options": "Email",
                    "reqd": 1,
                    "show_in_list": 1
                },
                {
                    "fieldname": "message",
                    "label": "Message",
                    "fieldtype": "Small Text",
                    "reqd": 1
                }
            ]
        })
        webform.insert(ignore_permissions=True)
        frappe.db.commit()
        print("✅ Contact Submission Web Form created successfully")
    else:
        print("ℹ️ Contact Submission Web Form already exists")
