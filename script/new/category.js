db.category.insert({
categoryName: "IT",
currentCategoryTree: "IT",
showpiority : "1"
});
db.category.insert({
categoryName: "IT-SoftWare",
parentCategory: db.category.find()[0],
currentCategoryTree: "IT",
showpiority : "1"
});
db.category.insert({
categoryName: "IT-HardWare",
parentCategory: db.category.find()[0],
currentCategoryTree: "IT",
showpiority : "1"
});
db.category.insert({
categoryName: "IT-Networking",
parentCategory: db.category.find()[0],
currentCategoryTree: "IT",
showpiority : "1"
});
db.category.insert({
categoryName: "IT-System",
parentCategory: db.category.find()[0],
currentCategoryTree: "IT",
showpiority : "1"
});
