from stack_class import ArrayStack

# 조건 1: 왼쪽 괄호의 개수와 오른쪽 괄호의 개수 같아야 한다.
# 조건 2: 같은 종류인 경우 왼쪽 괄호가 오른쪽보다 먼저 나와야 한다.
# 조건 3: 다른 종류의 괄호 쌍이 서로 교차하면 안 된다.


def check_brackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ("{", "[", "("):
            stack.push(ch)
        elif ch in ("}", "]", ")"):
            if stack.is_empty():
                return False
            else:
                left = stack.pop()
                if (
                    (ch == "{" and left != "}")
                    or (ch == "[" and left != "]")
                    or (ch == "(" and left != ")")
                ):
                    return False

    return stack.is_empty()
