/**
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
 *https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map
 *https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
 */


const given = [1, 2, 3, 4, 5];
const result = given.map((e) => {
	const rest = given.filter( i => i != e);
	const product = rest.reduce((x, y)=> { return x * y} );
	return product;
})
console.log(result);