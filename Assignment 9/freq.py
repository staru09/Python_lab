def find_word_with_highest_frequency(text):
    """
    Finds the word with the largest frequency and returns it with its frequency.
    In case of a tie in frequency, returns the longest word among those with the highest frequency.
    """
    words = text.lower().split()
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    max_frequency = max(word_freq.values())
    candidates = [word for word, freq in word_freq.items() if freq == max_frequency]
    
    result_word = max(candidates, key=len)
    
    return f"{result_word} {max_frequency}"

#input1 = "Work like you do not need money love like you have never been hurt and dance like no one is watching"
#input2 = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
#print(find_word_with_highest_frequency(input1))  
#print(find_word_with_highest_frequency(input2))  

text = input("Enter your text: ")
print(find_word_with_highest_frequency(text))  