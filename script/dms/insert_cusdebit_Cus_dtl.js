db.cus_debit.insert({
"cus_id" : db.customer.find()[0]._id,
"loan_type" : db.loan_type.find()[0]._id,
"month" : new Date(),
"debit" : 8000000,
"total_debit" : 8200800,
"cycle" : 4,
"payment" : 0,
"create_date" : new Date(),
"loan_date" : new Date(),
"last_close_date" : new Date(),
"status" : 1,
"note" : ""
});
db.cus_debit_detail.insert({
"cus_id" : db.customer.find()[0]._id,
"cus_debit_id" : db.cus_debit.find()[0]._id,
"from_date" : new Date(),
"to_date" : new Date(),
"rate" : 5000,
"start_cycle" : 6090450.75,
"amount" : 30452.25375,
"payment" : 0,
"end_cycle" : 6120903.00375,
"debit" : 0,
"status" : 1,
"days" : 1,
"create_date" : new Date(),
"flag" : 0,
"index" : 4
});