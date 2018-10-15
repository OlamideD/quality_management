// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quality Action', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frm.set_value("date", frappe.datetime.get_today())
		if (frm.doc.review != null){
			frm.set_value("type", "Quality Review")
		}
		else if(frm.doc.feedback != null){
			frm.set_value("type", "Customer Feedback")
		}
		else{
			frm.set_value("type", "Quality Review")
		}
	},
	review: function(frm){
		frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Quality Review",
				name: frm.doc.review
            },
            callback: function (data) {
				var review = "";
				console.log(data.message)
				for (var i = 0; i < data.message.values.length; i++ ){
					if (data.message.values[i].achieved < data.message.values[i].target){
						frm.add_child("description")
						
						//review = review + "For " + data.message.values[i].objective + ", Achieved Value : " + data.message.values[i].achieved + " is Less than Target Value " + data.message.values[i].target + "\n"; 
					}
				}
			//	frm.set_value("problem", review);
            }
        })
	},
	feedback: function(frm) {
		frappe.call({
			"method": "frappe.client.get",
			args: {
				doctype: "Customer Feedback",
				name: frm.doc.feedback
			},
			callback: function(data){
				for (var i = 0; i < data.message.feedback.length; i++ ){
					frm.add_child("description");
					frm.fields_dict.description.get_value()[i].problem = ""+ data.message.feedback[i].parameter +"-"+ data.message.feedback[i].qualitative_feedback;
				}
				frm.refresh();
			}
		})
	}
});
