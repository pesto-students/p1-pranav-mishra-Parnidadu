function hasDuplicate(arr){
    return new Set(arr).size !== arr.length 
}

// finding duplicates in numbers
console.log(hasDuplicate([1,2,3,4,5,5]))
console.log(hasDuplicate([1,2,3,4,5]))


// finding duplicates in letters
console.log(hasDuplicate(['a','b','c','d','a','']))
console.log(hasDuplicate(['a','b','c','d']))

// finding duplicates in string
console.log(hasDuplicate(['Pranav','Pranav','Mishra']))

console.log(hasDuplicate(['Pranav','Mishra']))
