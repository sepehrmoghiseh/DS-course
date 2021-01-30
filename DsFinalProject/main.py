class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class node:
    def __init__(self):
        data = None
        next = None


def add(data):
    newnode = node()
    newnode.data = data
    newnode.next = None
    return newnode


def string_to_SLL(text, head):
    head = add(text[0])
    curr = head

    for i in range(len(text) - 1):
        curr.next = add(text[i + 1])
        curr = curr.next

    return head


def insertAfter(courser, head, new_data):
    cur = head
    i = 2
    while i < courser:
        i += 1
        cur = cur.next
    if courser == 0:
        new_node = add(new_data)
        new_node.next = head
        return new_node
    elif courser == lentgh(head):
        while (cur.next != None):
            cur = cur.next
        new_node = add(new_data)
        cur.next = new_node
    else:
        new_node = add(new_data)
        new_node.next = cur.next.next
        cur.next.next = new_node
    return head


def delete(courser, head):
    cur = head
    i = 2
    while i < courser:
        i += 1
        cur = cur.next
    if cur == head:
        head.next = head.next.next
    elif cur.next.next == None:
        cur.next = None
    else:
        cur.next = cur.next.next

    return head


def lentgh(head):
    temp = head
    count = 0
    while (temp):
        count += 1
        temp = temp.next
    return int(count)


def convert_to_string(head):
    str = ""
    tmp = head
    while (tmp != None):
        str += tmp.data
        if (tmp.next != None):
            if ((tmp.next.data.isdigit() == False and tmp.data.isdigit() == True) or (
                    tmp.next.data.isdigit() == True and tmp.data.isdigit() == False) or (
                    tmp.next.data.isdigit() == False and tmp.data.isdigit() == False)):
                str += " "
        tmp = tmp.next

    return str


def convert_to_string2(head):
    str = ""
    tmp = head
    while (tmp != None):
        str += tmp.data
        tmp = tmp.next
    return str


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isdigit() == True:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2


def print_(head):
    curr = head
    while (curr != None):
        print((curr.data), end="")
        curr = curr.next


def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v
    return False


if __name__ == '__main__':
    d = [[] for _ in range(20)]
    courser = 0
    commands = input()
    if int(commands) < 1 or int(commands) > 300000:
        exit()
    string = input()
    str1 = None
    head = None
    head = string_to_SLL(string, head)
    str = convert_to_string(head)

    for i in range(0, int(commands)):
        cmd = input()
        if cmd == ">":
            if int(courser) < lentgh(head):
                courser += 1
        elif cmd == "<":
            if int(courser) > 0:
                courser -= 1
        elif "+" in cmd:
            cmd = cmd.replace("+ ", "")
            head = insertAfter(courser, head, cmd)
            str = convert_to_string(head)
            courser += 1
        elif "-" in cmd:
            head = delete(courser, head)
            str = convert_to_string(head)
            courser -= 1
        elif cmd == "?":
            str1 = convert_to_string2(head)
            str = convert_to_string(head)
            str1 = str1[:courser] + "|" + str1[courser:]
            print(str1)
        elif cmd == "!":
            str = infixToPostfix(str)
            s = search(d, str)
            if s:
                print(s)
            else:
                calculate = int(postfixEval(str) % (1000000007))
                insert(d, str, calculate)
                print(calculate)
