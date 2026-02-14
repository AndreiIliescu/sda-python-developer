// py -> print("something") => to display a message within terminal
// js -> console.log("something") => display a message within terminal / console (for browser)

console.log("Hello World!");
// Pt. a rula codul in terminal folosim comanda: "node <nume_fisier>.js"

// Comments:
// => js
// " # " => py
/*
    multi-line
    comments
    in
    js
    */

// Data Types in js compared with py:
// Primitive types: string, number, boolean, null, undefined, Symbol
// Reference types: Array, Object, Function, Set, Map

// py -> str (string) => "my string" (single quotes (''), double quotes ("" ))
// js -> string => "my string" (single quotes (''), double quotes ("" ), backticks (``))

// 3 metode de a defini o variabila in JS:
// const -> tipul varibilei este constant acelasi (nu mai poate fi reasignata)
// let -> decizi tipul de variabilei mai tarziu (poate fi reasignata ulterior)
// var -> nu prea se mai utilizeaza

// ex. primitive:
const firstName = "John"; // string
const lastName = new String(22); //string -> "22"

let age = 30; // number

const isAdmin = true; // boolean

let user = null; // null
user = "Jane Doe";

let car; // undefined
console.log(car);

// ex. reference:
const users = ["John Doe", "Jane Doe", "Will Smith"]; // Array
// js -> element => index si valoare
// py -> item => index si valoare

console.log(users[users.length - 1]); // Accesarea ultimului element din Array in js ("Will Smith")
// users[-1] => Accesarea ultimului element din lista in py ("Will Smith")
console.log(users[0]); // Accesarea primului element din Array in js ("John Doe")

// Metode pe Array:
users.push("David Martinez"); // Adaugat la final de Array
users.pop(); // Scoate/Sterge ultimul element din Array

// .map() creeaza un Array nou, deci el trebuie salvat mereu intr-o variabila
const newUsers = users.map((user, userIndex) => {
  return {
    id: userIndex,
    fullName: user,
  };
});
console.log(newUsers);

const person = {
  fullName: "Jane Doe",
  age: 25,
  isMarried: true,
  hobbies: ["hiking", "table tennis", "gym"],
  social: {
    facebookUrl: "https://facebook.com/john.doe",
    instagramUrl: ".....",
  },
}; // Object (echivalent: dictionare din Python)
// Accesarea proprietatilor din Obiect, folosind notatia . (dot):
console.log(person.age); // result => 30

function greetUser(user = "John") {
  return `Hello, ${user}!`;
}

const greet1 = greetUser();
const greet2 = greetUser("Emma");
console.log(greet1);
console.log(greet2);

// Conditional statement
// if, else if, else:
if (person.age >= 18) {
  console.log("Adult");
} else if (person.age >= 13) {
  console.log("Teenager");
} else {
  console.log("Child");
}

// switch:
switch (true) {
  case person.age >= 18:
    console.log("Adult");
  case person.age >= 13:
    console.log("Teenager");
  default:
    console.log("Invalid age");
}

// Loops:

// Basic for loop
for (let i = 0; i < 10; i++) {
  console.log("i = ", i);
}
// "i++" => incrementeaza cu 1 (echivalent din Pythin i += 1)

console.log();

// while loop
// "===" compara si valoarea dar si tipul ei de date
let n = 0;
while (n <= 10) {
  console.log("n = ", n);
  n++;
}
