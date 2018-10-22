// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Goal', {
	refresh: function(frm) {

	},
	revision: function(frm) {
		if(frm.doc.revised_on == null){
			frm.set_value("revised_on", frappe.datetime.get_today());
		}
	},
	measurable: function(frm) {
		frm.fields_dict.objective.grid.remove_all();
		if(frm.doc.measurable == "No"){
			frm.fields_dict.objective.grid.docfields[1].hidden = 1;
			frm.fields_dict.objective.grid.docfields[2].hidden = 1;
			frm.refresh();
		}
		else{
			frm.fields_dict.objective.grid.docfields[1].hidden = 0;
			frm.fields_dict.objective.grid.docfields[2].hidden = 0;
			frm.refresh();
		}
	}
});