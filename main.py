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
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            # Process closing bracket, write your code here
            last = opening_brackets_stack.pop()
            if opening_brackets_stack == []:
                return i + 1
            if are_matching(last.char, next) == "False":
                return i + 1


            
    print(opening_brackets_stack)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
