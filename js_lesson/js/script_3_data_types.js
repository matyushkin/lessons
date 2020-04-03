'use strict'; 

// JavaScript -- динамически типизированный язык
let message = "hello";
message = 123456;

// Числа: кроме обычных существуют: Infinity, -Infinity и NaN
alert( 1 / 0 ); // Infinity
alert( Infinity ); // Infinity
alert( "не число" / 2 ); // NaN, такое деление является ошибкой
alert( "не число" / 2 + 5 ); // NaN, любая операция с NaN возвращает NaN

// символ "n" в конце означает, что это BigInt
const big = 1234567890123456789012345678901234567890n;

// строки заключаются в одинарные, двойные или обратные кавычки
let str = "Привет";
let str2 = 'Одинарные кавычки тоже подойдут';
let phrase = `Обратные кавычки позволяют встраивать переменные ${str}`;

// Функционал обратных кавычек
let name = "Иван";
alert( `Привет, ${name}!` ); // Привет, Иван!
alert( `результат: ${1 + 2}` ); // результат: 3

// Булевый тип
let nameFieldChecked = true; // да, поле отмечено
let ageFieldChecked = false; // нет, поле не отмечено

let isGreater = 4 > 1;
alert( isGreater ); // true (результат сравнения)

// Значение null: ничего, пусто, значение неизвестно
let age = null;

// Значение undefined: значение не было присвоено
let x;
alert(x); // выведет "undefined"

/*Обычно null используется для присвоения переменной
«пустого» или «неизвестного» значения,
а undefined – для проверок, была ли переменная назначена.*/

// Как определить тип
typeof undefined // "undefined"
typeof 0 // "number"
typeof 10n // "bigint"
typeof true // "boolean"
typeof "foo" // "string"
typeof Symbol("id") // "symbol"
typeof Math // "object" - встроенный объект для математических операций и констант
typeof null // "object" - узаконенная ошибка языка
typeof alert // "function" 