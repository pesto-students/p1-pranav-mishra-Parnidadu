const mathOperations = require('./Calculator');
 
describe("Calculator Test", () => {
 test('adding 2 and 3 should return 5', () => {
   // arrange and act
   var result = mathOperations.sum(2,3)
 
   // assert
   expect(result).toBe(5);
 });
 
 test("subtract 40 from 100 = 60", () => {
   // arrange and act
   var result = mathOperations.diff(100,40)
 
   // assert
   expect(result).toBe(60);
 });
 
 test("multiply 5*25 should result in 125", () => {
   // arrange and act
   var result = mathOperations.product(5,25)
 
   // assert
   expect(result).toBe(125);
 });
})