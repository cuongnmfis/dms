
db.curriculumn_study_progress.remove()
db.curriculumn.remove()
db.material.remove()
db.action.remove()



db.customer.find({username:"mt1"})[0]._id
db.customer.find().forEach(printjson)
db.customer.find({cus_id:db.user.find({username:"cuongnm"})[0]._id}).forEach(printjson)
db.cus_debit.find({cus_id:db.user.find({username:"cuongnm"})[0]._id}).forEach(printjson)
db.cus_debit_detail.find({cus_debit_id:{cus_id:db.user.find({username:"cuongnm"})[0]._id}}).forEach(printjson)
db.user.find({username:"cuongnm"})[0].forEach(printjson)


db.user.find({username:"mt1"})[0].forEach(printjson)

mentor: mt1: ObjectId("53833c6930635f17c4daaaf1")

db.mentor.find({user:db.user.find({username:"mt1"})[0]._id}).forEach(printjson)

db.mentor.find({user:db.user.find({username:"mt1"})[0]._id})[0]._id

db.curriculumn.find({mentor: db.mentor.find({user:db.user.find({username:"mt1"})[0]._id})[0]._id}).forEach(printjson)

db.curriculumn_study_progress.find().forEach(printjson)
