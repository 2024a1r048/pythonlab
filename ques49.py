 #WAP to detect whether a comment is spam or not. a comment should be treated as sapm if it contains any of these keywords"make a lot of money","buy now","subscribe this"or"click this"

cmnt = input("Enter a comment: ")
cmnt = cmnt.lower()
if "make a lot of money" in cmnt or "subscribe this" in cmnt or "buy this" in cmnt or "click this" in cmnt:
    print("This comment is a spam.")
else:
    print("This is comment is not a spam.")