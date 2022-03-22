# Attribution for this code: https://fizzbuzzed.com/top-interview-questions-4/

import collections
import string

# beginWord - string, endWord - string, wordList - list of string
def ladderLength(beginWord, endWord, wordList):
    # We use q to keep track of the next nodes to process in the BFS.
    # Each item in the queue is a list with two items:
    #   item[0] = word
    #   item[1] = steps to reach word + 1 (i.e. number of nodes in list of nodes 
    #             traversed to reach word - (format of Word Ladder I output)).
    q = collections.deque([ [beginWord,1] ])
    # We keep track of words we've processed to avoid getting stuck in a loop.
    seen = set([beginWord])
    # wordList is given as a list but we want O(1) lookup so we convert to a set.
    wordList = set(wordList)
    while q:
        q_item = q.popleft()
        for candidate in generateNeighbors(q_item[0], wordList):
            if candidate == endWord:
                return q_item[1] + 1
            elif candidate in seen:
                continue
            seen.add(candidate)
            q.append([candidate, q_item[1] + 1])
    return 0


def generateNeighbors(word, wordList):
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in wordList:
                yield candidate


# Dfs to recreate the old paths. This takes a dictionary of parent pointers.
# The entries A -> B mean you can get to A from B in a bfs starting
# from beginWord. The outptu is a list of all paths from beginWord to word.
# {string -> string}, string, string
def createAllPaths(parentDict, word, beginWord):
    if word == beginWord:
        return [[beginWord]]
    output = []
    for w in parentDict[word]:
       x = createAllPaths(parentDict, w, beginWord)
       for l in x:
           l.append(word)
           output.append(l)
    return output

# beginWord - string
# endWord - string
# wordList - [ string ]
def allShortestLadders(beginWord, endWord, wordList):
    # We use q to keep track of the next nodes to process in the BFS.
    q = collections.deque([ beginWord ])
    # We keep track of words we've processed to avoid getting stuck in a loop.
    seen = set([beginWord])
    # Convert to set for O(1) lookup
    wordList = set(wordList)
    # We'll store word -> set(words) in this dictionary. The set will have all
    # words which we reached 'word' from during the bfs. Then, we can treat this as
    # an adjacency list graph and dfs it to create the output.
    parents = collections.defaultdict(set)
    while q:
        # We can't return as soon as we see an answer because we want to
        # return ALL shortest paths. We'll process level by level and only
        # return when we're done a full level.
        num_in_level = len(q)
        finished = False
        seen_this_level = set()
        for i in range(num_in_level):
            q_item = q.popleft()
            for candidate in generateNeighbors(q_item, wordList):
                if candidate == endWord:
                    finished = True
                elif candidate in seen:
                    continue
                if candidate not in seen_this_level:
                    q.append(candidate)
                seen_this_level.add(candidate)
                parents[candidate].add(q_item)
        if finished:
            break
        seen |= seen_this_level
    return createAllPaths(parents, endWord, beginWord)