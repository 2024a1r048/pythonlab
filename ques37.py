 # take a senetence containing double  spaces and unwanted spaces at begining end . Clean The sentence
s = input("Enter  a sentence:")
print(s)
s = s.strip()
s = s.replace("  "," ")
print(s)