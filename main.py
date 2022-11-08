Balanced_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}

Balanced_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
Unbalanced_list = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]
General_list=Balanced_list+Unbalanced_list

class Stack(list):

    def isEmpty(self):
        if not self:
            return True
        else:
            return False

    def push(self, element):
        self.append(element)

    def pop(self):
        if not self.isEmpty():
            element = self[-1]
            self.__delitem__(-1)
        return element

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def Ballance_check(symbol):
    stack = Stack()
    for element in symbol:
        if element in Balanced_dict:
            stack.push(element)
        elif element == Balanced_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()

if __name__ == '__main__':
    for element in General_list:
        print(f'{element:<25}{Ballance_check(element)}')