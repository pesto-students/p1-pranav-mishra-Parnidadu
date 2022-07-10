// using Async/Await and generator, create separate functions and achieve the same.

function resolveAfter1Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 1000);
    });
}

const generator = (function* () {
    const a = yield 5; // paused here
    // waiting for next()
})();

console.log(generator.next())


async function asyncCall() {
    const result = await resolveAfter1Seconds();
    let generatorValue1 = generator.next()
    let generatorValue2 = generator.next(10)
    return [result, generatorValue1, generatorValue2]
}

asyncCall()
    .then((res) => {
        console.log("res", res)
    })
    .catch((err) => {
        console.log(res)
    })
    .finally(() => {
        console.log("finally")
    })