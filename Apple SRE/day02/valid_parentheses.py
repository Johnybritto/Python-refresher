"""Day 2, P07: check whether brackets are correctly matched and nested."""


def is_valid(text: str) -> bool:
   

   bracket_map = {
       "}" : "{" , "]": "[" , ")" : "("
   }

   opening_map = set(["{", "(", "["])

   stack =[]
   for i in text:
       if i in opening_map:
           stack.append(i)
       elif stack and stack[-1] == bracket_map[i]:
           stack.pop()
       else:
           return False

   if stack:
       return False
   else:
       return True
    
           
    #"""Validate a string containing only ()[]{}. The empty string is valid."""
    ## TODO: Implement using a stack.
    #raise NotImplementedError("Implement is_valid before running the checks")


def run_tests() -> None:
    cases = [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("{[()]}", True),
        ("(]", False),
        ("([)]", False),
        ("(", False),
        (")", False),
        ("((", False),
        ("())", False),
        (")(", False),
    ]
    for text, expected in cases:
        assert is_valid(text) is expected, f"Failed for {text!r}"
    print("All Valid Parentheses checks passed")


if __name__ == "__main__":
    run_tests()
