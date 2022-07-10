const Fibo= (n)=>({
	[Symbol.iterator]:()=>{
  	let i=1;
    let prev = 0, nex= 0;
    return{
    	next:()=>{
      	if(i++<=n){
        	[prev, nex] = [nex,(prev+nex)|| 1];
          return {value: prev, done:false}
        }
        else{
        	return {done:true}
        }
      }
    }
  }
});

console.log([...Fibo(6)]);
for(let ele of Fibo(6)){
	console.log(ele);
}