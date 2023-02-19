# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
          

        if next in ")]}":
           if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            
            opening_brackets_stac.pop()
            
    if opening_brackets_stac:
        return opening_brackets_stac[0].position
    return "success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
