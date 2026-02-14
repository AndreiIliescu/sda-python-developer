import re


# Regex grouping
# Pentru a crea un grup folosim "()"
# OBS! - Daca vreti sa cautati "(" sau ")" in text trebuie puse sub forma "\(" sau \")"

text = "Thomas S. (33), was last seen in Bucharest."
pattern = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) (\(\d+\))"

match = re.match(pattern, text)
print(match)
print(match.groups())
print()

text = "Thomas S. (33), Eva M. (35), was last seen in Bucharest."
match = re.findall(pattern, text)
print(match)
