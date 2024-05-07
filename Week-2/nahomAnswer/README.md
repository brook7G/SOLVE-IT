#Fourier Transform Challenge

after reading and researching alot the only solution i founded that was relativly optimal and easier to understand was to use numpy and calculate the sequence using the forier transformer built in numpy and i won't lie this isn't my best work but i hope it it acceptable as the challenge requires a great amount of math 






# Word ladder

let's take this as an example to better explain 

####wordLadder('hit','cog',["hot","dot","dog","lot","log","cog"])

so the world ladder problem requires a bfs or breathfirst seach which basically means we have to check all the nodes before procceding to the next there for 
firs we check if the end word is in the worldlist because if not then there is no amount of steps to reach it hence returning 0



so now we create a set of the list. we will have the set to look up and then we use a queue so basically as i have said bfs is an algorithm that checks all it's negihbors before procceding to another so we initialize the beginword let's say beginWord = 'hit'and the level of modification is 1 and after that we will have a var called front this would help us check if we don't have a next matching pair to break out of the loop and. 




so while our front is less than length of queue or the word i would have have to iterate through. i will then assign the current word and level to the index of front and in our case or first example current word would be hot and the level would be 1 we would increment front as we have used our first element in the queue then we check if current word is same as our endWord we would return the ammount of steps(level) but if not we would have to change some of the letter of the word and check again so in the for loop we have will have another for loop to check every possiblity so in the first case it would check if hit => ait and check if it is in the wordSet and if it is we would have to remove the word and start again after adding the next word and incrementing the level by one and if not then we would go through the values again and again and at last if hit going through series of modifications result in cog we would return out level 


hope this explains it well... you can comment if i have to do more explanation.
