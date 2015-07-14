def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    Letter2 = []
    import string
    for char in string.ascii_lowercase:
        Letter2.append(char)
        
        
    def removeDuplicate(Letter1,Letter2):
        Letter1Start = Letter1[:]
        for char2 in Letter1Start:
            if char2 in Letter2:
                Letter2.remove(char2)
        return ''.join(str(char2) for char2 in Letter2)
    
    return removeDuplicate(lettersGuessed,Letter2)
