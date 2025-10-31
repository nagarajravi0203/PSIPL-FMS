import frappe

def after_install():
    """Run after app is installed"""
    create_module_def()
    create_contact_submission_webform()


def create_module_def():
    """Ensure Module Def for PSIPL FMS exists"""
    if not frappe.db.exists("Module Def", "PSIPL FMS"):
        frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "PSIPL FMS",
            "app_name": "psipl_fms"
        }).insert(ignore_permissions=True)
        frappe.db.commit()
        print("✅ Module Def 'PSIPL FMS' created successfully")
    else:
        print("ℹ️ Module Def 'PSIPL FMS' already exists")


def create_contact_submission_webform():
    """Create the Contact Submission Web Form if not exists"""
    if not frappe.db.exists("Web Form", {"route": "contact-submission"}):
        webform = frappe.get_doc({
            "doctype": "Web Form",
            "module": "PSIPL FMS",
            "title": "Contact Submission",
            "route": "contact-submission",
            "web_form_name": "contact_submission",
            "is_standard": 0,
            "published": 1,
            "login_required": 0,
            "doc_type": "Contact Submission",
            "web_form_fields": [
                {
                    "fieldname": "full_name",
                    "label": "Full Name",
                    "fieldtype": "Data",
                    "reqd": 1
                },
                {
                    "fieldname": "email",
                    "label": "Email",
                    "fieldtype": "Data",
                    "options": "Email",
                    "reqd": 1
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
