def insertAtBottom(stack, element):
    if len(stack)==0:
        stack.append(element)
        return
    top = stack.pop()
    insertAtBottom(stack, element)
    stack.append(top)



def ReverseStack(stack):
    if len(stack) == 0:
        return
    popped = stack.pop()
    ReverseStack(stack)
    insertAtBottom(stack, popped)



stack = [1,2,3,4]
result = []
ReverseStack(stack)
print(stack)