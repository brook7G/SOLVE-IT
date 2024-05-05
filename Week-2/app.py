import numpy as np
from collections import deque

def fft(sequence):
    N = len(sequence)
    if N <= 1:
        return sequence
    even = fft(sequence[0::2])
    odd = fft(sequence[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

def word_ladder_length(start, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return 0
    
    queue = deque([(start, 1)])
    visited = set()
    
    while queue:
        word, length = queue.popleft()
        if word == end:
            return length
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i+1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    
    return 0

def fourier_transform_menu():
    print(" Fourier Transform ")
    sequence = input("Enter a sequence of complex numbers separated by spaces: ").split()
    sequence = [complex(num) for num in sequence]
    result = fft(sequence)
    print("Fourier Transform:", result)

def word_ladder_menu():
    print("Word Ladder ")
    start_word = input("Enter the start word: ")
    end_word = input("Enter the end word: ")
    word_list = input("Enter a list of words separated by spaces: ").split()
    length = word_ladder_length(start_word, end_word, word_list)
    print("Shortest sequence length:", length)

def main():
    while True:
        print("\nMenu:")
        print("1. Fourier Transform Challenge")
        print("2. Word Ladder Challenge")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            fourier_transform_menu()
        elif choice == '2':
            word_ladder_menu()
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()
