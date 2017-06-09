def file_read(file_name):
        fr = open(file_name, 'r')
        each_line = fr.readlines()
        print(each_line)
        line = [x.strip('\n') for x in each_line]
        print(line)
        assign_val(line)

def assign_val(list):
        type = list[0]
        start = list[1]
        goal = list[2]
        d= {}
        for i in range(1, int(list[3]) + 1):
            (key, val, cost) = list[i+3].split()
            print(key, val, cost)
            if key in d.keys():
                d[key][val] = cost
            else:
                d[key] = {}
                d[key][val] = cost
            print(d)
        g = [d]
        print(g)

      # line1 = lines.split(:\\n")

file_read('sample.txt')