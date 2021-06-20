# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    emails = []

    for name in S.split(";"):
        name = name.strip(" ")
        names = name.split(" ")
        if len(names)>2:
            first, middle, last = names
        else:
            first,  last = names
        last = last.replace("-", "")
        
        head = first.lower() + "." + last.lower()
        mail = head + "@" + C.lower() + ".com"
        if mail not in emails:
            emails.append(mail)
        else:
            for i in range(2, 10000):
                mail = head + str(i) +"@" + C.lower() + ".com"
                if mail not in emails:
                    emails.append(mail)
                    break
    
    result = "; ".join(emails)

    return result