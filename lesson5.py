
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def display(self):
        print("{}-{}-{}-{}".format(self.surface, self.base, self.pos, self.pos1))
    
def lesson40():
    print("- 係り受け解析結果の読み込み(形態素)")
    p = "../neko.txt.cabocha"
    line_num = 3
    s = ""
    result = []
    r = []
    i = 1
    with open(p, "r") as f:
        for line in f.readlines():
            if "EOS" in line:
                if r:
                    result.append(r)
                    r = []
                continue
            elif "空白" in line:
                continue
            else:
                if "*" != line[0]:
                    line = line[:-1]
                    surface, datas = line.split("\t")
                    datas = datas.split(",")
                    r.append(Morph(surface, datas[6], datas[0], datas[1]))
    result3 = result[3-1]
    for r in result3:
        r.display()

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

def lesson41():
    print("- 係り受け解析結果の読み込み(文節・係り受け)")
    p = "../neko.txt.cabocha"
    line_num = 3
    s = ""
    result = []
    r = []
    i = 1
    with open(p, "r") as f:
        for line in f.readlines():
            if "EOS" in line:
                if r:
                    result.append(r)
                    r = []
                continue
            elif "空白" in line:
                continue
            else:
                if "*" != line[0]:
                    line = line[:-1]
                    surface, datas = line.split("\t")
                    datas = datas.split(",")
                    r.append(Morph(surface, datas[6], datas[0], datas[1]))
    
    
def lesson42():
    pass

def lesson43():
    pass

def lesson44():
    pass

def lesson45():
    pass

def lesson46():
    pass

def lesson47():
    pass

def lesson48():
    pass

def lesson49():
    pass

if __name__ == "__main__":
    lesson40()
    lesson41()
    lesson42()
    lesson43()
    lesson44()
    lesson45()
    lesson46()
    lesson47()
    lesson48()
    lesson49()
