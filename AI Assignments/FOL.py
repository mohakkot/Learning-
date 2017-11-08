import copy
import string
import random
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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Predicate():
    def __init__(self):
        self.name = ''
        self.argsList = []
        self.operator = False
        self.argsCount = 0
        self.type = True
        self.new = False

class Clause():
    def __init__(self):
        self.node = Predicate()
        self.left = None
        self.right = None
        self.id = []
        self.match = []


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
        self.resolution()
        self.fout.close()
        self.fin.close()

    def read_qcnt(self):
        return(self.fin.readline())

    def read_query(self):
        for i in range(self.qcnt):
            self.sentence = self.infixToPostfix(self.fin.readline())
            self.query.append(self.create_kb(self.sentence))

    def read_kbcnt(self):
        return (self.fin.readline())

    def read_kb(self):
        for i in range(self.kbcnt):
            self.sentence = self.infixToPostfix(self.fin.readline())
            self.select_keys = set()
            self.kb.append(self.create_kb(self.sentence))
        self.clause_split()

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
        while i < (len(s)):
            if s[i] == ' ':
                i = i + 1
                continue
            if s[i] == '\n':
                i+=1
                continue
            if s[i] == '=':
                token = s[i] + s[i + 1]
                i = i + 1
            else:
                token = s[i]
            k = i + 1
            if token.isupper():
                for j in range(k, len(s)):
                    word = s[j]
                    if word == '\n':
                        j=j+1
                        continue
                    if word not in ['|', '&', '=']:
                        if word == ' ':
                            j = j + 1
                            i = i + 1
                            continue
                        if (s[j] == ')' and s[j - 1] == ')'):
                            break
                        else:
                            token = token + word
                            i += 1
                    else:
                        break

                postfixList.append(self.add_predicate(token))

            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
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
                postfixList.append(self.add_predicate(ch))
        return(postfixList)

    def add_predicate(self, token):
        tpred = Predicate()
        root = Clause()
        i = 0
        n = ''
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
        while token[i] != ')' or i < len(token)-1:
            if token[i] == ',':
                tpred.argsList.append(a)
                tpred.argsCount = tpred.argsCount + 1
                a = ''
            elif token[i] == ' ':
                pass
            else:
                a = a + token[i]
            i = i + 1
        tpred.argsList.append(a)
        tpred.argsCount = tpred.argsCount + 1
        root.node = tpred
        return(root)

    def create_kb(self, sent):
        i = 0
        while i < len(sent):
            if sent[i].node.operator:
                if sent[i].node.name == '|' or sent[i].node.name == '&':
                    sent[i].left = sent[i-2]
                    sent[i].right = sent[i-1]
                    sent = sent[0:i-2] + sent[i:]
                    i = i-2
                if sent[i].node.name == '=>':
                    sent[i-2] = self.negate(sent[i-2])

                    sent[i].node.name = '|'
                    sent[i].right = sent[i-1]
                    sent[i].left = sent[i-2]
                    sent = sent[0: i-2]+ sent[i:]
                    i = i-2
                if sent[i].node.name == '~':
                    if sent[i-1].node.operator:
                        sent[i] = self.negate(sent[i-1])
                        sent = sent[0: i-1] + sent[i:]
                    else:
                        if sent[i-1].node.type:
                            sent[i-1].node.type = False
                        else:
                            sent[i-1].node.type = True
                        sent = sent[0:i] + sent[i+1:]
                    i = i-1

            i= i +1
        sent = self.standardize(sent[0])
        sent = self.distribute(sent)
        return(sent)

    def negate(self, root):
        if not root.node.operator:
            if root.node.type:
                root.node.type = False
            else:
                root.node.type = True
            return(root)

        else:
            if root.node.name == '|':
                root.node.name = '&'
            else:
                root.node.name = '|'

            self.negate(root.left)
            self.negate(root.right)
            return(root)

    def distribute(self, data):

            if data.node.name == '|' and data.left.node.name == '&' and not data.right.node.operator:
                data.node.name = '&'
                value = Clause()
                value.node.name = data.right.node.name
                value.node.argsList = data.right.node.argsList
                value.node.argsCount = data.right.node.argsCount
                value.node.type = data.right.node.type
                value.node.operator =  data.right.node.operator
                data.right.node.name = '|'
                data.right.node.type = 'True'
                data.right.node.operator = 'True'
                data.right.node.argsList = []
                data.right.node.argsCount = 0
                nl = self.distribute(data.left.left)
                nr = self.distribute(data.left.right)
                data.left.node.name = '|'
                data.left.left = nl
                data.right.left = nr
                data.left.right= value
                data.right.right= value

            if data.node.name == '|' and data.right.node.name == '&' and not data.left.node.operator:
                data.node.name = '&'
                value = Clause()
                value.node.name = data.left.node.name
                value.node.argsList = data.left.node.argsList
                value.node.argsCount = data.left.node.argsCount
                value.node.type = data.left.node.type
                value.node.operator = data.left.node.operator

                data.left.node.name = '|'
                data.left.node.type = 'True'
                data.left.node.operator = 'True'
                data.left.node.argsList = []
                data.left.node.argsCount = 0
                nl = self.distribute(data.right.left)
                nr = self.distribute(data.right.right)
                data.right.node.name = '|'

                data.right.left = nr
                data.left.left = nl
                data.right.right = value
                data.left.right = value


            if data.node.name == '|' and data.right.node.name == '&' and data.left.node.name == '&':
                data.node.name = '&'
                nl1 = self.distribute(data.left.left)
                nr1 = self.distribute(data.left.right)
                nl2 = self.distribute(data.right.left)
                nr2 = self.distribute(data.right.right)

                data.left.left = Clause()
                data.left.left.node.name = '|'
                data.left.left.node.type = 'True'
                data.left.left.node.operator = 'True'
                data.left.left.node.argsList = []
                data.left.left.node.argsCount = 0
                data.left.right = Clause()
                data.left.right.node.name = '|'
                data.left.right.node.type = 'True'
                data.left.right.node.operator = 'True'
                data.left.right.node.argsList = []
                data.left.right.node.argsCount = 0
                data.left.left.left = nl1
                data.left.left.right = nl2
                data.left.right.left = nl1
                data.left.right.right = nr2

                data.right.left = Clause()
                data.right.left.node.name = '|'
                data.right.left.node.type = 'True'
                data.right.left.node.operator = 'True'
                data.right.left.node.argsList = []
                data.right.left.node.argsCount = 0
                data.right.right = Clause()
                data.right.right.node.name = '|'
                data.right.right.node.type = 'True'
                data.right.right.node.operator = 'True'
                data.right.right.node.argsList = []
                data.right.right.node.argsCount = 0
                data.right.left.left = nr1
                data.right.left.right = nl2
                data.right.right.left = nr1
                data.right.right.right = nr2

            return data

    def standardize(self, root):
        self.stand_key = {}
        self.findnode(root)
        return root

    def findnode(self, clause):
        if clause.left != None:
            self.findnode(clause.left)
        if clause.right != None:
            self.findnode(clause.right)
        if clause.left == None and clause.right== None:
            for i in range(clause.node.argsCount):
                if not clause.node.argsList[i][0].isupper():
                    if clause.node.argsList[i] in self.stand_key.keys():
                        clause.node.argsList[i] = self.stand_key[clause.node.argsList[i]]
                    else:
                        sub = self.id_generator()
                        while True:
                            if sub in self.select_keys:
                                sub = self.id_generator()
                            else:
                                break
                        self.stand_key[clause.node.argsList[i]] = sub
                        clause.node.argsList[i] = sub
                        self.select_keys.add(sub)

    def ordering(self):
        for i in range(len(self.operkb)):
            if self.order(self.operkb[i]):
                self.operkb.insert(0, self.operkb[i])
                self.operkb.__delitem__(i+1)

    def order(self, clause):
        if clause.left != None:
            self.order(clause.left)
        if clause.right != None:
            self.order(clause.right)
        if clause.left == None and clause.right == None:
            for i in range(clause.node.argsCount):
                if clause.node.argsList[i][0].isupper():
                    return True
        return False



    def id_generator(self):
        chars = string.ascii_lowercase + string.digits
        final = ''
        for _ in range(3):
            a = random.choice(chars)
            final = final + a
        return final


    def clause_split(self):
        j = 0
        while j < (len(self.kb)):
            self.split_AND(self.kb[0])
            self.kb = self.kb[1:]
            j += 1
        self.kbcnt = len(self.kb)


    def split_AND(self, clause):
        if clause.node.operator and clause.node.name == '&':
            self.split_AND(clause.left)
            self.split_AND(clause.right)
        else:
            self.kb.append(clause)

    def resolution(self):
        for i in range(self.qcnt):
            if self.query[i].node.type:
                self.query[i].node.type = False
            else:
                self.query[i].node.type = True
            self.operkb = []
            for j in range(len(self.kb)):
                temp = copy.deepcopy(self.kb[j])
                self.operkb.append(temp)
            self.operkb.append(self.query[i])
            self.ordering()
            m = 0
            self.list_arr =[]
            while m < len(self.operkb):
                check = False
                if(self.operkb[m].node.new):
                    j = 0
                else:
                    j = m+1
                while(j < len(self.operkb)):
                    if m == j:
                        j += 1
                        continue
                    if m not in self.operkb[j].match or j not in self.operkb[m].match:
                        if(self.resolve(self.operkb[m], self.operkb[j])):
                            self.write_output('TRUE')
                            check = True
                            break
                        self.operkb[j].match.insert(0, m)
                        self.operkb[m].match.insert(0, j)
                    j+=1
                    if len(self.operkb) > 400:
                        break
                if j!= len(self.operkb):
                    break
                m += 1
                if len(self.operkb) > 400:
                    break
            if not check:
                result = 'FALSE'
                self.write_output(result)
                check =  False


    def write_output(self, result):
        self.fout.write(result + '\n')



    def resolve(self, clause1, clause2):
            clauselist1 = []
            self.find_clauselist(clause1, clauselist1)
            clauselist2 = []
            self.find_clauselist(clause2, clauselist2)
            i=0
            while i < len(clauselist1):
                j=0
                while j < len(clauselist2):
                    if clauselist1[i].node.name == clauselist2[j].node.name and \
                                    clauselist1[i].node.type != clauselist2[j].node.type:
                        if clause2.id != () and hash(clause1) in clause2.id:
                            return False
                        if clause1.id != () and hash(clause2) in clause1.id:
                            return False

                        self.key_set ={}
                        if self.unify(clauselist1[i].node.argsList, clauselist2[j].node.argsList):
                            if (len(clauselist1) == 1 and len(clauselist2) == 1):
                                return True
                            else:
                                c1 = self.copyfrom(clause1)
                                c2 = self.copyfrom(clause2)
                                if (len(clauselist1) == 1):
                                    c1 = None
                                else:
                                    c1 = self.deletenode(c1, clauselist1[i])
                                if (len(clauselist2) == 1):
                                    c2 = None
                                else:
                                    c2 = self.deletenode(c2, clauselist2[j])
                                clauselist1 = clauselist1[0:i] + clauselist1[i+1:]
                                i-=1
                                clauselist2 = clauselist2[0:j] + clauselist2[j+1:]
                                j-=1
                                new_prd =Predicate()
                                new_prd.name = '|'
                                new_prd.operator = True
                                new_cls = Clause()
                                new_cls.node = new_prd
                                new_cls.left = c1
                                new_cls.right = c2
                                h1 = (hash(clause1))
                                h2 = (hash(clause2))
                                if c1 != None:
                                    h3 = (hash(c1))
                                    new_cls.id.append(h3)
                                if c2 != None:
                                    h4 = (hash(c2))
                                    new_cls.id.append(h4)
                                new_cls.id.append(h1)
                                new_cls.id.append(h2)
                                if clause1.id != []:
                                    for a in range(len(clause1.id)):
                                        new_cls.id.append(clause1.id[a])
                                if clause2.id != []:
                                    for a in range(len(clause2.id)):
                                        new_cls.id.append(clause2.id[a])
                                self.operkb.append(new_cls)
                                return False
                    j+=1
                i+=1

    def copyfrom(self, root):
        if root == None:
            return root
        tcls = Clause()
        tpred = Predicate()
        tpred.name = root.node.name
        tpred.type = root.node.type
        tpred.argsCount = root.node.argsCount
        tpred.operator = root.node.operator
        tpred.new = root.node.new
        if root.node.argsCount != 0:
            for i in range(root.node.argsCount):
                tpred.argsList.append(root.node.argsList[i])
        else:
            tpred.argsList = []
        tcls.node = tpred
        for j in range(len(root.id)):
            tcls.id.append(root.id[j])
        tcls.left = self.copyfrom(root.left)
        tcls.right = self.copyfrom(root.right)
        return tcls

    def unify(self, args1, args2):
        if args1 == [] and args2 == []:
            return False
        for i in range(len(args1)):
            if args1[i][0].isupper() and args2[i][0].isupper():
                if args1[i] != args2[i]:
                    return False
            elif args1[i][0].isupper() and not args2[i][0].isupper():
                 self.key_set[args2[i]] = args1[i]
            elif not args1[i][0].isupper() and args2[i][0].isupper():
                 self.key_set[args1[i]] = args2[i]
            elif not args1[i][0].isupper() and not args2[i][0].isupper():
                 self.key_set[args1[i]] = args2[i]
        if i == len(args1)-1:
            return True
        else:
            return False


    def deletenode(self, clause, tobedel):
        if clause.left != None:
            clause.left = self.deletenode(clause.left, tobedel)
        if clause.right != None:
            clause.right = self.deletenode(clause.right, tobedel)
        if (clause.left == None and clause.right== None):
            if((not clause.node.operator) and (clause.node.name == tobedel.node.name) and \
                                        (clause.node.argsCount == tobedel.node.argsCount) and \
                                        (clause.node.type == tobedel.node.type)):
                for i in range(tobedel.node.argsCount):
                    if tobedel.node.argsList[i] != clause.node.argsList[i]:
                        break
                if i == tobedel.node.argsCount-1:
                    return None
                else:
                    for k in range(clause.node.argsCount):
                        if clause.node.argsList[k] in self.key_set.keys():
                            clause.node.argsList[k] = self.key_set[clause.node.argsList[k]]
            elif (not clause.node.operator):
                for k in range(clause.node.argsCount):
                    if clause.node.argsList[k] in self.key_set.keys():
                        clause.node.argsList[k] = self.key_set[clause.node.argsList[k]]
        return clause


    def find_clauselist(self, root, clist):
        ret_list = []
        if root.left != None and root.node.operator:
            self.find_clauselist(root.left,clist)
        if root.right != None and root.node.operator:
            self.find_clauselist(root.right,clist)
        if root.right == None and root.left == None and not root.node.operator:
            clist.append(root)





run = Driver('input.txt')
run.read_file()
