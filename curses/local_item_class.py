def item_class_clear():
    global c
    c = []

def item_class_init(head, content):
    global c
    c.append({"head": head, "content": content})
    return(len(c)-1)  # return id -PR-

def item_class_get(i):
    global c
    return(c[i]["content"])
