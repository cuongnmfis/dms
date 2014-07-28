db.progress_type.update(
   { _id: ObjectId("53cf93dbb6cc1799847f65cc") },
   {
      progressName:"ちょうどスタート",
      progressDescription:"ちょうどスタート",
      rate: 0
   },
   { upsert: true }
);

db.progress_type.update(
   { _id: ObjectId("53cf93dcb6cc1799847f65cd") },
   {
      progressName:"まだ始まったばかり",
      progressDescription:"まだ始まったばかり",
      rate: 15
   },
   { upsert: true }
);

db.progress_type.update(
   { _id: ObjectId("53cf93ddb6cc1799847f65ce") },
   {
      progressName:"少し高度な",
      progressDescription:"少し高度な",
      rate: 25
   },
   { upsert: true }
);

db.progress_type.update(
   { _id: ObjectId("53cf93ddb6cc1799847f65cf") },
   {
      progressName:"ハーフ進捗",
      progressDescription:"ハーフ進捗",
      rate: 50
   },
   { upsert: true }
);

db.progress_type.update(
   { _id: ObjectId("53cf93deb6cc1799847f65d0") },
   {
      progressName:"ほぼ完全な",
      progressDescription:"ほぼ完全な",
      rate: 85
   },
   { upsert: true }
);

db.progress_type.update(
   { _id: ObjectId("53cf93deb6cc1799847f65d1") },
   {
      progressName:"完全な",
      progressDescription:"完全な",
      rate: 100
   },
   { upsert: true }
);
db.progress_type.find().forEach(printjson).order_by('rate')