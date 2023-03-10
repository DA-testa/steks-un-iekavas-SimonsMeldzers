# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):

        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            
            if opening_brackets_stack == []:
                return i + 1

            last = opening_brackets_stack.pop()
            if are_matching(last.char, next) == False:
                return i + 1
            pass

    if opening_brackets_stack == True:
        last = opening_brackets_stack.pop()
        return last.position + 1
    return 0


def main():
    text = input().strip()

    if text == "F":
        file = input().strip()
        text = open(file).read().strip()
    elif text == "I":
        text = input().strip()
    else:
        return

    mismatch = find_mismatch(text)
    
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)



if __name__ == "__main__":
    main()
