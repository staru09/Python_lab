import re

poem = """If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain."""

count_v = len(re.findall(r'v', poem))
print(count_v)

poem_single_line = re.sub(r'\n', ' ', poem)
#print(poem_single_line)

poem_replace_ch_co = re.sub(r'\bch', 'Ch', poem, flags=re.IGNORECASE)
poem_replace_ch_co = re.sub(r'\bco', 'Co', poem_replace_ch_co, flags=re.IGNORECASE)
#print(poem_replace_ch_co)

poem_replace_ai_hi = re.sub(r'(ai|hi)(.{0,3})', r'\1*\*', poem)
#print(poem_replace_ai_hi)
