db.curriculumn.remove();

db.curriculumn.insert({
duration : 1,
duration_type : "Week",
from_date : ISODate("2014-05-01T00:00:00Z"),
material : [db.material.find()[0]._id,db.material.find()[1]._id,db.material.find()[2]._id,db.material.find()[3]._id],
mentor : db.mentor.find()[0]._id,
name : "初心者のためのクラウドサービス",
published_date : ISODate("2014-05-16T18:34:20.588Z"),
to_date : ISODate("2014-05-16T00:00:00Z"),
units : [ ],
action : [db.action.find()[0]._id,db.action.find()[1]._id,db.action.find()[2]._id]
});

db.curriculumn.insert({
duration : 1,
duration_type : "Week",
from_date : ISODate("2014-05-01T00:00:00Z"),
material : [db.material.find()[0]._id,db.material.find()[1]._id],
mentor : db.mentor.find()[0]._id,
name : "How to become Oracle Master",
published_date : ISODate("2014-05-16T18:34:20.588Z"),
to_date : ISODate("2014-05-16T00:00:00Z"),
units : [ ],
action : [db.action.find()[0]._id,db.action.find()[1]._id]
});
db.curriculumn.insert({
duration : 1,
duration_type : "Week",
from_date : ISODate("2014-05-01T00:00:00Z"),
material : [db.material.find()[3]._id,db.material.find()[4]._id],
mentor : db.mentor.find()[0]._id,
name : "Curriculumn name",
published_date : ISODate("2014-05-16T18:34:20.588Z"),
to_date : ISODate("2014-05-16T00:00:00Z"),
units : [ ],
action : [db.action.find()[0]._id,db.action.find()[1]._id]
});
db.curriculumn.insert({
duration : 1,
duration_type : "Week",
from_date : ISODate("2014-05-01T00:00:00Z"),
material : [db.material.find()[5]._id],
mentor : db.mentor.find()[0]._id,
name : "初心者のためのクラウドサービス",
published_date : ISODate("2014-05-16T18:34:20.588Z"),
to_date : ISODate("2014-05-16T00:00:00Z"),
units : [ ],
action : [db.action.find()[0]._id,db.action.find()[1]._id,db.action.find()[2]._id]
});
