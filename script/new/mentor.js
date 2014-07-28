db.mentor.remove();

db.mentor.insert({
user:db.user.find()[0]._id
});
db.mentor.insert({
user:db.user.find()[1]._id
});
db.mentor.insert({
user:db.user.find()[2]._id
});
