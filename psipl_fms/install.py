import frappe

def after_install():
    # create Module Def if not exists
    if not frappe.db.exists("Module Def", "PSIPL FMS"):
        frappe.get_doc({"doctype":"Module Def", "module_name":"PSIPL FMS", "app_name":"psipl_fms"}).insert(ignore_permissions=True)
        frappe.db.commit()
