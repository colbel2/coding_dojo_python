// binarySearch(input, target ... ?)
// two parameters - an array of sorted integers to search through (input)
// and an integer to search for (target)
// return true if the target integer is found in the array and false otherwise
// there are two other parameters that get defaults, can you figure them out?
// we gotta do this recursively!
// this will have a big O time complexity of log n
// https://www.bigocheatsheet.com/


function binarySearch(input, target, parameter_a = null, parameter_b = null) {
    // figure out what paramater_a and parameter_b are
    // their defaults are not null

}

input = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]

console.log(binarySearch(input, 1));
console.log(binarySearch(input, 2));
console.log(binarySearch(input, 3));
console.log(binarySearch(input, 4));
console.log(binarySearch(input, 5));
console.log(binarySearch(input, 6));
console.log(binarySearch(input, 7));
console.log(binarySearch(input, 8));
console.log(binarySearch(input, 10));
console.log(binarySearch(input, 11));
console.log(binarySearch(input, 12));

console.log(binarySearch(input, -1));
console.log(binarySearch(input, 24));
console.log(binarySearch(input, 9));