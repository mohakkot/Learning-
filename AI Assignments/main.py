from pythonds.basic.stack import Stack

class Predicate():
    def __init__(self):
        self.name = ''
        self.argsList = []
        self.operator = False
        self.argsCount = None
        self.type = True

        # self.pid = Predicate.id
        # Predicate.id = Predicate.id + 1
        # self.type = None

class Clause():
    def __init__(self):
        self.node = Predicate()
        self.left = None
        self.right = None


class Driver():
    def __init__(self, filename):
        self.input = filename
        self.output = 'output.txt'
        self.query = []
        self.qcnt = 0
        self.kbcnt = 0
        self.kb = []

    def read_file(self):
        self.fin= open(self.input, 'r')
        self.fout = open(self.output,'w')
        self.qcnt = int(self.read_qcnt())
        self.read_query()
        self.kbcnt = int(self.read_kbcnt())
        self.read_kb()
        self.distribute(self.kb)

    def read_qcnt(self):
        return(self.fin.readline())

    def read_query(self):
        for i in range(self.qcnt):
            self.query.append(self.fin.readline())

    def read_kbcnt(self):
        return (self.fin.readline())

    def read_kb(self):
        for i in range(self.kbcnt):
            self.sentence = self.infixToPostfix(self.fin.readline())
            #print(self.sentence)
            self.kb.append(self.create_kb(self.sentence))
            print(self.kb)

    def infixToPostfix(self, s):
        prec = {}
        prec["~"] = 5
        prec["&"] = 4
        prec["|"] = 3
        prec["=>"] = 2
        prec["("] = 1
        opStack = Stack()
        postfixList = []
        i = 0
        while i != (len(s) - 1):
            if s[i] == ' ':
                i = i + 1
                continue
            if s[i] == '=':
                token = s[i] + s[i + 1]
                i = i + 1
            else:
                token = s[i]
            k = i + 1
            # print(token)
            if token.isupper():
                for j in range(k, len(s) - 1):
                    word = s[j]
                    #not word.isupper() and
                    if word not in ['|', '&', '=']:
                        if word == ' ':
                            j = j + 1
                            i = i + 1
                            continue
                        if (s[j] == ')' and s[j - 1] == ')'):
                            continue
                        else:
                            token = token + word
                            i += 1
                    else:
                        break

                postfixList.append(self.add_predicate(token))

                #postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    #print(topToken)
                    postfixList.append(self.add_predicate(topToken))
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                        (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(self.add_predicate(opStack.pop()))
                opStack.push(token)
            i = i + 1
        while not opStack.isEmpty():
            ch = opStack.pop()
            if ch != '(':
                postfixList.append(self.add_predicate(opStack.pop()))
        return(postfixList)

    def add_predicate(self, token):
        tpred = Predicate()
        root = Clause()
        i = 0
        n = ''
        #print(token)
        if token in ['|', '&', '=>', '~']:
            tpred.name = token
            tpred.operator = True
            root.node = tpred
            return(root)
        while token[i] != '(':
            n = n + token[i]
            i = i + 1
        if token[i] == '(':
            tpred.name = n
            tpred.operator = False
            i = i + 1
        a = ''
        while token[i] != ')':
            if token[i] == ',':
                tpred.argsList.append(a)
                a = ''
            elif token[i] == ' ':
                pass
            else:
                a = a + token[i]
            i = i + 1
        tpred.argsList.append(a)
        root.node = tpred
        return(root)

    def create_kb(self, sent):
        i = 0
        while i < len(sent):
            if sent[i].node.operator:
                if sent[i].node.name == '|' or sent[i].node.name == '&':
                    sent[i].left = sent[i-2]
                    sent[i].right = sent[i-1]
                    sent = sent[i:]
                    i = i-2
                if sent[i].node.name == '=>':
                    if sent[i-2].node.operator:
                        sent[i-2] = self.negate(sent[i-2])

                    sent[i].node.name = '|'
                    sent[i].right = sent[i-1]
                    sent[i].left = sent[i-2]
                    sent = sent[i:]
                    i = i-2
                if sent[i].node.name == '~':
                    if sent[i-1].node.operator:
                        sent[i] = self.negate(sent[i-1])
                        sent = sent[i:]
                    else:
                        if sent[i-1].node.type:
                            sent[i-1].node.type = False
                        else:
                            sent[i-1].node.type = True
                        sent = sent[0:i] + sent[i+1:]
                    i = i-1

            i= i +1
        return(sent)

    def negate(self, root):
        if root.node.name == '|':
            root.node.name = '&'
        else:
            root.node.name = '|'
        if root.left.node.type:
            root.left.node.type = False
        else:
            root.left.node.type = True
        if root.right.node.name:
            root.right.node.type = False
        else:
            root.right.node.type = True
        return(root)

    def distribute(self, data):

run = Driver('input.txt')
run.read_file()
