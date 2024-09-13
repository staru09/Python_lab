'''def tr(srcstr, dststr, string):
    translation_dict = {src: dst for src, dst in zip(srcstr, dststr)}
    translated_string = ''.join(translation_dict.get(char, char) for char in string)
    return translated_string

srcstr = 'abc'
dststr = 'mno'
string = 'abcdef'
print(tr(srcstr, dststr, string))'''

def tr(srcstr, dststr, string):
    translation_dict = {src: dst for src, dst in zip(srcstr, dststr)}
    
    delete_chars = set(srcstr[len(dststr):])
    
    translated_string = ''.join(translation_dict.get(char, char) for char in string if char not in delete_chars)
    
    return translated_string

srcstr = 'abcdef'
dststr = 'mno'
string = 'abcdefghi'
print(tr(srcstr, dststr, string))

