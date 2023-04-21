 //  Komment
 console.log('Hello World!');
 
 let name = 'Változó';
 console.log(name);
 let firtName = 'Keresztnév';
 let lastName = 'Családnév';

 let interestRate = 0.3;
 interestRate = 1;
 console.log(interestRate);

 let s = 'String'; //String
 let age = 30; //Number
 let isApproved = false; //boolen
 let firstName = undefined;
 

 console.log(typeof(s));
 let person = {
    name: 'Peti',
    age: 30
 }

//Dot Nottation
 person.name = 'John';

//Bracket Notation
let selection = 'name';
 person[selection] = 'Mary';

 console.log(person);

let selectedColor = ['red', 'blue'];
selectedColor[2] = 1;
console.log(selectedColor.length);
// Performing a task
function greet(name, lastName) {
  console.log('Hello ' + name+ ' ' + lastName);
}
// Calculating a valut
function square(number) {
    return number * number;
}

let number = square(2);
console.log(number)
greet('John','Smith');
greet('Mary');