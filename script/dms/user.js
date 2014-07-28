db.customer.insert({
	_id: db.user.find({username:"cuongnm"})[0]._id,
	cus_code = db.user.find({username:"cuongnm"})[0].username,
	first_name = db.user.find({username:"cuongnm"})[0].first_name,
	last_name = db.user.find({username:"cuongnm"})[0].last_name,
	full_name = db.user.find({username:"cuongnm"})[0].first_name + db.user.find({username:"cuongnm"})[0].last_name,
	id_no = "111519954",
	address = "Ha Noi",
	home_address = "",
	fone_number = "0977868788",
	create_date = new date(),
	status = 1,
	about = "This is cuongNM infomation"
});
