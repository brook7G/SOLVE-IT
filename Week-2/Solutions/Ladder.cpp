#include <iostream>
#include <unordered_set>
#include <queue>

using namespace std;

// Function to find the length of the shortest sequence of transformations
int shortestWordLadder(const string& start, const string& end, const unordered_set<string>& wordList) {
    // Check if the end word is not in the word list
    if (wordList.find(end) == wordList.end())
        return 0;
    
    // Queue for BFS traversal, each element stores the current word and its corresponding length of transformation sequence
    queue<pair<string, int>> q;
    q.push({start, 1});
    
    // BFS traversal
    while (!q.empty()) {
        string currentWord = q.front().first;
        int currentLength = q.front().second;
        q.pop();
        
        // If current word is the end word, return its transformation sequence length
        if (currentWord == end)
            return currentLength;
        
        // Try all possible transformations of the current word
        for (int i = 0; i < currentWord.length(); ++i) {
            char originalChar = currentWord[i];
            for (char c = 'a'; c <= 'z'; ++c) {
                if (c == originalChar)
                    continue;
                currentWord[i] = c;
                // If the transformed word is in the word list, enqueue it with the incremented length of transformation sequence
                if (wordList.find(currentWord) != wordList.end()) {
                    q.push({currentWord, currentLength + 1});
                    wordList.erase(currentWord); // Remove the word from the list to avoid revisiting
                }
            }
            currentWord[i] = originalChar; // Revert back the change
        }
    }
    
    return 0; // If no transformation sequence is found
}
