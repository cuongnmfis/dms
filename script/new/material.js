db.material.remove();

db.material.insert({
published_date : new Date(),
unit : db.unit.find()[0]._id,
type : db.material_type.find()[0]._id,
name : "material name 001",
description: "When we arrive at Aomori Airport’s terminal building to meet with the airport director, the board hanging behind the information counters near the first floor entrance shows numerous flights have been canceled. With the entire surrounding area covered in white and snow falling steadily everywhere,…",
url : "http://www.amazon.com/Project-Management-Lite-Enough-Nothing/dp/1478129220/ref=sr_1_1?s=books&ie=UTF8&qid=1400148734&sr=1-1&keywords=project+management",
code : "ABC"
});

db.material.insert({
published_date : new Date(),
unit : db.unit.find()[0]._id,
type : db.material_type.find()[0]._id,
name : "material name 002",
description: "material name 002  material name 001  material name 001  material name 001  material name 001  material name 001  material name 001 ",
url : "http://www.amazon.com/Project-Management-Lite-Enough-Nothing/dp/1478129220/ref=sr_1_1?s=books&ie=UTF8&qid=1400148734&sr=1-1&keywords=project+management",
code : "ABC"
});

db.material.insert({
published_date : new Date(),
unit : db.unit.find()[0]._id,
type : db.material_type.find()[0]._id,
name : "material name 003",
description: "material name 003",
url : "http://www.amazon.com/Project-Management-Lite-Enough-Nothing/dp/1478129220/ref=sr_1_1?s=books&ie=UTF8&qid=1400148734&sr=1-1&keywords=project+management",
code : "ABC"
});

db.material.insert({
published_date : new Date(),
unit : db.unit.find()[0]._id,
type : db.material_type.find()[0]._id,
name : "material name 004",
description: "material name 004",
url : "http://www.amazon.com/Project-Management-Lite-Enough-Nothing/dp/1478129220/ref=sr_1_1?s=books&ie=UTF8&qid=1400148734&sr=1-1&keywords=project+management",
code : "ABC"
});

db.material.insert({
published_date : new Date(),
unit : db.unit.find()[0]._id,
type : db.material_type.find()[0]._id,
name : "material name 005",
url : "http://www.amazon.com/Project-Management-Lite-Enough-Nothing/dp/1478129220/ref=sr_1_1?s=books&ie=UTF8&qid=1400148734&sr=1-1&keywords=project+management",
code : "ABC"
});
