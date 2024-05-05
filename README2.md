## Introduction

This repository contains my solutions to the Week-2 coding challenge, which includes two challenges: the Fourier Transform challenge and the Word Ladder challenge.

## Fourier Transform Challenge

### Description

The Fourier Transform challenge involves implementing a function to perform a Fourier transform on a sequence of complex numbers using the Fast Fourier Transform (FFT) algorithm.

### Solution

I implemented the FFT algorithm in Python using a recursive approach. The function takes a sequence of complex numbers as input and returns the Fourier transform of the input sequence. The main steps of the FFT algorithm are:

1. Divide the sequence into even and odd indices.
2. Recursively compute the FFT of the even and odd subsequences.
3. Combine the results using twiddle factors to compute the final Fourier transform.

The solution is implemented in the `fft()` function in the `app.py` file.

## Word Ladder Challenge

### Description

The Word Ladder challenge involves finding the length of the shortest sequence of transformations from a start word to an end word, where only one letter can be changed at a time and each transformed word must exist in a given list of words.

### Solution

I implemented a breadth-first search (BFS) algorithm to solve the Word Ladder problem. The function takes the start word, end word, and a list of words as input and returns the length of the shortest sequence of transformations. The algorithm explores all possible transformations using one-letter changes until it reaches the end word.

The solution is implemented in the `word_ladder_length()` function in the `app.py` file.

## Usage

To use the solutions:

1. Clone this repository to your local machine.
2. Navigate to the repository directory.
3. Run the `app.py` file.
4. Choose between the Fourier Transform and Word Ladder challenges from the menu.
5. Follow the prompts to input the required information.
6. View the output.

## Dependencies

The solutions do not require any external dependencies and should work with a standard Python installation.
