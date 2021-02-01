var containsDuplicate = function(nums){
    nums.sort()
    for(let i = 0; i < nums.length -1 ; i++){
        if(nums[i] == nums[i+1]) return true
    }
    return false
}
var x= [1,1,1,3,3,4,3,2,4,2]
console.log(containsDuplicate(x))









// const input = [
//     "animal/mammal/dog",
//     "animal/mammal/cat/tiger",
//     "animal/mammal/cat/lion",
//     "animal/mammal/elephant",
//     "animal/reptile",
//     "plant/sunflower",
//   ];
// let splitIntoNames = input.map((str) => str.split("/"));
// function addName(element, list, index) {
//     if (index >= list.length) {
//       return;
//     }
//     let name = list[index];
//     let isEndOfList = index === list.length - 1;
  
//     element[name] = element[name] || (isEndOfList ? true : {});
  
//     addName(element[name], list, index + 1);
//   }
  
//   let result = {};
//   splitIntoNames.forEach((list) => {
//     addName(result, list, 0);
//   });
//   console.log("result:", JSON.stringify(result, null, 2));


// var input = ['animal/mammal/dog', 'animal/mammal/cat/tiger', 'animal/mammal/cat/lion', 'animal/mammal/elephant', 'animal/reptile', 'plant/sunflower'];

// result = (buildObj = (array, Obj = {}) => {
//   array.forEach((val) => {
//     keys = val.split('/');
//     (nestedFn = (object) => {
//       outKey = keys.shift();
//       object[outKey] = object[outKey] || {};
//       if (keys.length == 0) object[outKey] = true;
//       if (keys.length > 0) nestedFn(object[outKey]);
//     })(Obj)
//   })
//   return Obj;
// })(input);

// console.log(result);

let input = [
    "animal/mammal/dog",
    "animal/mammal/cat/tiger",
    "animal/mammal/cat/lion",
    "animal/elephant",
    "animal/reptile",
    "plant/sunflower",
  ];
  
//   let convertInput = (i = []) =>
//     i.reduce((prev, currItem = "") => {
//       let pointer = prev;
//       currItem.split("/").reduce((prevPre, currPre, preIdx, arrPre) => {
//         if (!pointer[currPre]) {
//           pointer[currPre] = preIdx === arrPre.length - 1 ? true : {};
//         }
//         pointer = pointer[currPre];
//       }, {});
//       return prev;
//     }, {});
  
//   console.log(JSON.stringify(convertInput(input), null, 4));

