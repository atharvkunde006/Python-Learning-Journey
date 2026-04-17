#
import re
pattern = r"cat"
text = "The cat is in the hat"
matches = re.findall(pattern, text)
print(matches)

##
import re
pattern= r"[a-z]+at"
text="The cat is in the hat"
matches= re.findall(pattern,text)
print(matches)

