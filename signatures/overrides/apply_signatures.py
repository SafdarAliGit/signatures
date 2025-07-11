import frappe

def purchase_order_update_signature_on_submit(doc, method):
    try:
        # More reliable field existence check
        meta = frappe.get_meta(doc.doctype)
        if not meta.has_field('custom_user_signature'):
            return

        # Get Signs document - improved query
        signs = frappe.get_value("Signs",
                                filters={"user": frappe.session.user},
                                fieldname="signature")
        
        if signs:
            # Update the Sales Invoice
            doc.db_set("custom_user_signature", signs)
            
    except Exception as e:
        frappe.logger().error(f"Error updating signature: {str(e)}")


def gate_outward_pass_update_signature_on_submit(doc, method):
    try:
        # More reliable field existence check
        meta = frappe.get_meta(doc.doctype)
        if not meta.has_field('user_signature'):
            return

        # Get Signs document - improved query
        signs = frappe.get_value("Signs",
                                filters={"user": frappe.session.user},
                                fieldname="signature")
        
        if signs:
            # Update the Sales Invoice
            doc.db_set("user_signature", signs)
            
    except Exception as e:
        frappe.logger().error(f"Error updating signature: {str(e)}")