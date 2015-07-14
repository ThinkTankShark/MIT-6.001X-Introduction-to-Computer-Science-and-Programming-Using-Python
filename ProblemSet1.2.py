def find_substring (word, string):
       count = 0
       len_word = len(word)
       for index in range(len(string) -1):
              if string[index : index + len_word] == word:
                          count += 1
       return count
       
              
              
