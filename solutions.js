// FizzBuzz
function runFizzBuzz() {
    let result = "";
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            result += "FizzBuzz ";
        } else if (i % 3 === 0) {
            result += "Fizz ";
        } else if (i % 5 === 0) {
            result += "Buzz ";
        } else {
            result += i + " ";
        }
    }
    document.getElementById("result").innerText = result;
}

// Palindrome Checker
function runPalindromeChecker() {
    const inputString = prompt("Enter a string to check for palindrome:");
    const processedString = inputString.toLowerCase().replace(/[^a-z0-9]/g, '');
    const reversedString = processedString.split('').reverse().join('');
    const isPalindrome = processedString === reversedString;
    document.getElementById("result").innerText = `Palindrome Check for "${inputString}": ${isPalindrome}`;
}

// Factorial Calculator
function runFactorialCalculator() {
    const number = parseInt(prompt("Enter a number to calculate its factorial:"));
    let factorial = 1;
    for (let i = 1; i <= number; i++) {
        factorial *= i;
    }
    document.getElementById("result").innerText = `Factorial of ${number}: ${factorial}`;
}

// Simple Calculator
function runSimpleCalculator() {
    const num1 = parseFloat(prompt("Enter the first number:"));
    const operator = prompt("Enter the operator (+, -, *, /):");
    const num2 = parseFloat(prompt("Enter the second number:"));
    let result;
    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        default:
            result = "Invalid operator";
    }
    document.getElementById("result").innerText = `Result: ${result}`;
}

// String Reversal
function runStringReversal() {
    const inputString = prompt("Enter a string to reverse:");
    const reversedString = inputString.split('').reverse().join('');
    document.getElementById("result").innerText = `Reversed String: ${reversedString}`;
}
