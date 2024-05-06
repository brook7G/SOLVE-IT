#Fourier Transform Challenge

import numpy as np

def fft1(input_sequence):
    output_sequence = np.fft.fft(input_sequence)
    return output_sequence



# WORD LADDER


def wordLadder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    wordSet = set(wordList)
    queue = [(beginWord, 1)]
    front = 0
    
    while front < len(queue):
        current_word, level = queue[front]
        front += 1
        if current_word == endWord:
            return level
        
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, level + 1))
                    
    return 0









