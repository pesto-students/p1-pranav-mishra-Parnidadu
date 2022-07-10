var fullName = {
    firstname: 'Pranav',
    lastname: 'Mishra',
    getName: function() {
        var name = this.firstname + ' ' + this.lastname;
        return name;
    }
};

var getFullName = function(snack, meal) {
    console.log(this.getName() + ' loves ' + snack + ' and ' + meal);
};

fn = getFullName.bind(fullName,'rice', 'dal');
fn()  // output will be rice and dal.
fn.call('biryani','veg'); // No change in the output, it will show rice and dal.
fn.apply(['biryani','non-veg'])   // No change in the output, it will show rice and dal.

getFullName.call(fullName,'biryani', 'dal');  //output will be biryani and dal
getFullName.apply(fullName,['roti', 'sabji']); // output will be roti and sabji.
