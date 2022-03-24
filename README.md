# Word Ladder
#### Video Demo:  <URL HERE>
#### Description: A game where you transform the start word to the end word one letter at a time.

"Word Ladder" is a popular kid's game often taught in reading classes. The rules are simple: Given a start word and an end word with the same number of letters, transform the start word to the end word by changing one letter at a time.

For example, suppose the start word is TRUCK and the end word is WHINE. A sample word ladder might be:

TRUCK -> TRICK -> THICK -> THINK -> THINE -> WHINE

The mechanics of the game were inspired by Wordle: 

* Each day, the game displays a new start word and end word, each five letters long.
* In between the start and end word are six boxes. Only the first box is active to start. The player must enter a word that is one letter different from the previous word (in this case, the start word). 
* Once players enter a valid word, the next box becomes active.
* If a player enters the end word in one of the boxes, they win, and their last box turns green.
* If the play does not enter the end word by the sixth and final guess, they lose and the last box turns red.


For this project, I created the game as a webpage, coded entirely in HTML, CSS, and Javascript. To generate the valid start and end words for the game, I used Python script. The next few sections describe how I used each technology in more detail.

## HTML
The game is included on a single web page, written in a file named index.html. I used the Bootstrap frameword to help with the design. The layout is simple:

* A navbar containing the name of the website: "Word Ladder"
* A section for displaying the error messages. These get dynamically added via JavaScript when a user makes an error.
* A section containing the start word, input boxes, and end word. These sections are all blank and populated via JavaScript.

## CSS
The CSS is stored in a styles.css file. I used a spare black-and-white style, so the CSS is not complicated. Some components of interest:
* The input boxes use the "text-transform: uppercase" style so that players can enter either uppercase or lowercase letters, but what they enter always appears in uppercase.
* The message boxes use @keyframes that make the boxes fade in and out when a player makes an error. This concept was new to me and took some research.

## JavaScript
This is the heart of the game. The JavaScript performs several steps:
1. Define the word lists and the games for each day.
   * The word lists are stored in the JavaScript and were taken from Wordle (credit: NYT). There are two word list: One containing common five-letter words, which are used to select the start and end words, and one containing all possible guesses.
   * The games are stored in a JSON object of key-value pairs, where each key is an integer from 0 to 365, representing a day of the year, and the values are two-element lists of [startWord, endWord] pairs.
2. Get the current game from the JSON file based on today's date.
3. Populate the start word and end word using the DOM.
4. Populate the game boxes and enable the first one, all using the DOM. The number of boxes and word length are hard-coded at 6 and 5, but these could be made configurable in the future.
5. Use an event listener to check when the player has pressed "Enter" to enter a guess.
6. Validate each guess and flash an error message if appropriate. Error messages include when the player enters:
   * Fewer than 5 letters.
   * A word not in the word list.
   * A word that differs by more than (or less than) 1 letter.
The form itself restricts non-letters and typing more than 5 letters, but the JavaScript contains additional error-checking in case someone decided to mess with the HTML.
7. Process the guess to see if the user won, lost, or moves to the next guess.

This code primarily relies on the manipulating the DOM.

## Python
I used Python to help generate the start and end words. First I needed to find valid word ladder games. This was a perfect candidate for a breadth first search algorithm, which excels at finding the shortest path between two locations, in this case the locations being the start and end word. Developing this algorithm was outside my current skillset, but luckily I was able to find one online that I could reuse(credit: fizzbuzzed.com). I stored this algorithm in the ladders.py file.

Then, I wrote a generated_games.py script to call the algorithm to generate the start and end words. This script does the following:

1. Define the Wordle word list (only the common words used in Wordle games, not the list of all valid guesses).
2. Choose two random words to use as the start and end words.
3. Run the breadth-first search algorithm to generate all the shortest paths. For example, if the game can be solved in 3 steps, then the algorithm returns all 3-step paths.
4. If the shortest paths are between 4 and 6 steps, it's suitable for inclusion on the site. Add the start and end word to a dictionary with this format: {dayOfYear: [start,end], ... }.
5. Once 366 games have been generated (one per year), export it to a JSON file.

This JSON file is what I used to copy in the game. In the future, I can see generating games dynamically rather than storing them. That would enable the user to refresh and always ensure they'd get a valid game. 