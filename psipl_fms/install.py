import frappe

def after_install():
    """Run after app is installed"""
    create_module_def()
    create_contact_submission_webform()
    create_lead_entry_webform()


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

def create_lead_entry_webform():
    """Create the Lead Entry Web Form if not exists"""
    if not frappe.db.exists("Web Form", {"route": "lead-entry"}):
        webform = frappe.get_doc({
            "doctype": "Web Form",
            "module": "CRM",
            "title": "Lead Entry",
            "route": "lead-entry",
            "web_form_name": "lead_entry",
            "is_standard": 0,
            "published": 1,
            "login_required": 0,
            "allow_edit": 0,
            "allow_multiple": 0,
            "show_attachments": 0,
            "doc_type": "Lead Entry",
            "web_form_fields": [
                {"fieldname": "customer_phone_number", "label": "Contact Number", "fieldtype": "Data", "reqd": 0},
                {"fieldname": "email", "label": "Email", "fieldtype": "Data", "reqd": 0},
                {"fieldname": "lead_type", "label": "Lead Type", "fieldtype": "Select", "options": "Hot Lead\nWarm Lead\nCold Lead"},
                {"fieldname": "company_name", "label": "Company Name", "fieldtype": "Select", "options": "1 BY 2 FOODS PRIVATE LIMITED\nA SQUARE EQUIPMENTS"},
                {"fieldname": "contact_person", "label": "Contact Person", "fieldtype": "Data"},
                {"fieldname": "customer_type", "label": "New / Old Customer", "fieldtype": "Select", "options": "Old customer - Direct Order (CRR)\nNew customer - Fresh Lead (NBD)\nOld customer - Fresh Lead (NBD CRR)\nP - Old customer - Fresh Lead (P - NBD CRR)"},
                {"fieldname": "segment", "label": "Segment", "fieldtype": "Select", "options": "Kiosk\nMall / Cinemas\nHotel\nRetail\nCafe\nKitchen Equipment Company\nIT / Corporate company\nDealer Enquiry\nSME (small medium enterprise)\nConsultant\nRestaurant\nBakery\nIndustrial Canteen\nTea / coffee shop\nFood Processing Industry\nFood Service Company\nOthers"},
                {"fieldname": "user_email", "label": "User Email", "fieldtype": "Data"},
                {"fieldname": "source_of_lead", "label": "Source of Lead", "fieldtype": "Select", "options": "Phone\nWhats App\nEmail\nIn person\nExhibition\nYou Tube\nIndia Mart\nWeb Site\nInstagram"},
                {"fieldname": "referral_name", "label": "Referral Name", "fieldtype": "Data"},
                {"fieldname": "location", "label": "Location", "fieldtype": "Data"},
                {"fieldname": "requirement", "label": "Requirement", "fieldtype": "Data"},
                {"fieldname": "lead_assigned_to", "label": "Lead Assigned To", "fieldtype": "Select", "options": "Melvin\nGoutham\nRajesh\nRamanathan\nUmesh\nDealer\nKavi Anand\nSC NBD and P-NBD CRR\nDevelopment Team\nKarthik\nSudhir Nayak\nZia\nSc (sharmila)\nYesuraja\nDarshan\nMurali Krishnan\nCRM (NBD CRR)\nSpare CRM\nSc NBD CRR\nTamilNadu\nAP and Telangana\nMaharashtra\nKarnataka"},
                {"fieldname": "dealer_name", "label": "Dealer Name", "fieldtype": "Select", "options": "CROCKERY WORLD\nHOTEL WORLD"},
                {"fieldname": "need_analysis", "label": "Need Analysis", "fieldtype": "Select", "options": "Required\nNot Required"},
                {"fieldname": "category", "label": "Category", "fieldtype": "Select", "options": "I Brew\nKitchen Equipment\nPots and pans\nI Brew + Kitchen Equipment\nAll the above\nDelibo\nSpares"},
                {"fieldname": "have_you_met_the_client", "label": "Have you met the client?", "fieldtype": "Select", "options": "Voice Call\nVideo Call\nIn Person\nNo"},
                {"fieldname": "is_demo_done", "label": "Is Demo Done?", "fieldtype": "Select", "options": "Yes\nNo"},
                {"fieldname": "next_step", "label": "Next Step", "fieldtype": "Select", "options": "Need to Meet\nRequired Quotation\nGive Demo\nUpdate in OTD\nRequired PI\nInvalid lead\nAssign to Dealer\nFuture Prospective Lead"},
                {"fieldname": "price_details", "label": "Price Details", "fieldtype": "Select", "options": "Maximum Selling Price\nRe-seller Price\nList Price\nDealer Price\nNot Applicable\nService provider price"},
                {"fieldname": "payment_status", "label": "Payment Status", "fieldtype": "Select", "options": "Credit customer\nAdv before production-bal before dispatch\nAdv before production-bal on Credit\n100 Percentage Advance before dispatch\nAdvance payment\nNot Applicable\nIntimate When Stock is Available"},
                {"fieldname": "current_location", "label": "Current Location", "fieldtype": "Data"},
                {"fieldname": "upload_image", "label": "Upload Image", "fieldtype": "Data"}
            ]
        })
        webform.insert(ignore_permissions=True)
        frappe.db.commit()
        print("✅ Lead Entry Web Form created successfully")
    else:
        print("ℹ️ Lead Entry Web Form already exists")