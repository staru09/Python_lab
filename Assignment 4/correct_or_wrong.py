def find_correct(spellings_dict):
    result = [0, 0, 0]
    
    for correct_spelling, contestant_spelling in spellings_dict.items():
        if len(correct_spelling) != len(contestant_spelling):
            result[2] += 1
        else:
            incorrect_count = sum(1 for c, s in zip(correct_spelling, contestant_spelling) if c != s)
            if incorrect_count == 0:
                result[0] += 1 
            elif incorrect_count <= 2:
                result[1] += 1  
            else:
                result[2] += 1
    
    return result

spellings_dict = {
    "THEIR": "THERE",
    "BUSINESS": "BISINESS",
    "WINDOWS": "WINDMILL",
    "WERE": "WEAR",
    "SAMPLE": "SAMPLE"
}

result = find_correct(spellings_dict)
print("Correct:", result[0])
print("Almost Correct:", result[1])
print("Wrong:", result[2])
