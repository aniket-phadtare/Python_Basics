stack=[]
MAX=5
def push(item):
    if len(stack)==MAX:
        print("stack Overflow")
    else:
        stack.append(item)
        print(item,"inserted")

def pop():
    if len(stack)==0:
        print("Stack Underflow")
    else:
        item=stack.pop()
        print("Delete Element:",item)

def peek():
    if len(stack)==0:
        print("Stack is Empty")
    else:
        print("Top element:",stack[-1])

def display():
    if len(stack)==0:
        print("Stack is Empty")
    else:
        print("Stack Elements:",stack[::-1])

push(10)
push(20)
push(30)
push(40)
push(50)
display()
peek()
pop()
display()
