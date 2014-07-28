db.category.remove();
db.category.insert({
categoryName: "IT",
currentCategoryTree: "IT",
showpiority : "1",
isparent : "1",
});
db.category.insert({
categoryName: "IT-Manager",
parentCategory: db.category.find()[0]._id,
currentCategoryTree: "IT",
showpiority : "1",
isparent : "0",
});
db.category.insert({
categoryName: "IT-Coding",
parentCategory: db.category.find()[0]._id,
currentCategoryTree: "IT",
showpiority : "1",
isparent : "0",
});
db.category.insert({
categoryName: "Car Driver Licence",
currentCategoryTree: "Licence",
showpiority : "1",
isparent : "1",
});
db.category.insert({
categoryName: "A1 - Licence",
parentCategory: db.category.find()[3]._id,
currentCategoryTree: "Licence",
showpiority : "1",
isparent : "0",
});
db.category.insert({
categoryName: "A2 - Licence",
parentCategory: db.category.find()[3]._id,
currentCategoryTree: "Licence",
showpiority : "1",
isparent : "0",
});
db.category.insert({
categoryName: "Maketing",
currentCategoryTree: "Maketing",
showpiority : "1",
isparent : "1",
});
db.category.insert({
categoryName: "PR",
parentCategory: db.category.find()[6]._id,
currentCategoryTree: "Maketing",
showpiority : "1",
isparent : "0",
});
db.category.insert({
categoryName: "Advertising",
parentCategory: db.category.find()[6]._id,
currentCategoryTree: "Maketing",
showpiority : "1",
isparent : "0",
});
db.category.insert({
categoryName: "Looby",
parentCategory: db.category.find()[6]._id,
currentCategoryTree: "Maketing",
showpiority : "1",
isparent : "0",
});