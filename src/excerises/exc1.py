
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    closeTag=False
    lastOpenTag=0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            lastOpenTag=i+1
                      
            
        if next in ")]}":
            # Process closing bracket, write your code here
            top=opening_brackets_stack.pop()
            closeTag=True

            if not are_matching(top,next):
                return i+1

    if closeTag==False:
        return lastOpenTag
    return "Success"







