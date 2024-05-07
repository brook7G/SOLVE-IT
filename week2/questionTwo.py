from collections import deque

def shortest_sequence_length(start, end, words):
    
    if end not in words:
        return 0
    
    queue = deque([(start, 0)])  # Initialize the queue with the start word and its length (1)
    visited = set([start])       # Initialize a set to keep track of visited words
    
    while queue:
        word, length = queue.popleft()  # Dequeue the word and its length
        if word == end:
            return length
        # Generate all possible next words by changing one letter
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i+1:]
                # If the next word is in the list of words and hasn't been visited yet
                if next_word in words and next_word not in visited:
                    queue.append((next_word, length + 1))  # Enqueue the next word with updated length
                    visited.add(next_word)                 # Mark the next word as visited
    return 0  # If no transformation sequence exists

# Test the function
start = "hit"
end = "cog"
words =  ["hot", "dot", "dog", "lot", "log", "cog"]
''''
The explanation for this question is:
hit -> hot .... this is one step
hot -> dot ..... this is the second transformation
dot -> dog .... this is the third transformation
dog -> cog  .... this is the fourth transfomration

Therefore the above example outputs 4

'''
print(shortest_sequence_length(start, end, words))  # Output: 4



''''

The solution employs a breadth-first search (BFS) algorithm to systematically explore possible word transformations 
from a start word to an end word, ensuring that each transformation changes only one letter at a time and the transformed word exists 
in a given list. By maintaining a queue of word sequences and tracking visited words, it efficiently identifies the shortest transformation sequence. 
If no valid sequence is found, it returns 0.


'''
