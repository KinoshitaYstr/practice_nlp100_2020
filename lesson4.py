import json
import matplotlib.pyplot as plt
import numpy as np

def lesson30():
    print("- 形態素解析結果の読み込み")
    p = "../neko.txt.mecab"
    result = []
    r = []
    with open(p, "r") as f:
        for line in f.readlines():
            line = line[:-1]
            datas = line.split("\t")
            if "EOS" != datas[0]:
                details = datas[1].split(",")
                dic = {}
                dic["surface"] = datas[0]
                dic["base"] = details[6]
                dic["pos"] = details[0]
                dic["pos1"] = details[1]
                r.append(dic)
            else:
                if r:
                    result.append(r)
                r = []
    # for r in result:
        # print("============================-")
        # for v in r:
            # print(v)
    print(result)

def get_morphological_analysis_result():
    p = "../neko.txt.mecab"
    result = []
    r = []
    with open(p, "r") as f:
        for line in f.readlines():
            line = line[:-1]
            datas = line.split("\t")
            if "EOS" != datas[0]:
                details = datas[1].split(",")
                dic = {}
                dic["surface"] = datas[0]
                dic["base"] = details[6]
                dic["pos"] = details[0]
                dic["pos1"] = details[1]
                r.append(dic)
            else:
                if r:
                    result.append(r)
                r = []
    return result

def lesson31():
    print("- 動詞")
    datas = get_morphological_analysis_result()
    for data in datas:
        for val in data:
            if "動詞" == val["pos"]:
                print(val["surface"])

def lesson32():
    print("- 動詞の原型")
    datas = get_morphological_analysis_result()
    for data in datas:
        for val in data:
            if "動詞" == val["pos"]:
                print("{} -> {}".format(val["surface"], val["base"]))

def lesson33():
    print("- 「AのB」")
    datas = get_morphological_analysis_result()
    no_flag = False
    for data in datas:
        for val in data:
            if no_flag and val["surface"] != "の" and "名詞" == before_val["pos"] and "名詞" == val["pos"]:
                print("{}の{}".format(before_val["surface"], val["surface"]))
                no_flag = False
                before_val = val
            if val["surface"] == "の":
                no_flag = True
            else:
                before_val = val
            

def lesson34():
    print("- 名詞の連接")
    datas = get_morphological_analysis_result()
    r = ""
    for data in datas:
        r = ""
        for val in data:
            if val["pos"] == "名詞":
                # print("-", val["surface"])
                r = r+val["surface"]
            elif not r:
                r = ""
            else:
                print(r)
                r = ""

def lesson35():
    print("- 単語の出現頻度")
    datas = get_morphological_analysis_result()
    dic = {}
    for data in datas:
        for val in data:
            if val["base"] in dic:
                dic[val["base"]] = dic[val["base"]]+1
            else:
                dic[val["base"]] = 1
    result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(result)

def get_vocaburary_rank():
    datas = get_morphological_analysis_result()
    dic = {}
    for data in datas:
        for val in data:
            if val["base"] in dic:
                dic[val["base"]] = dic[val["base"]]+1
            else:
                dic[val["base"]] = 1
    result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return result

def lesson36():
    print("- 頻度上位10位")
    datas = get_vocaburary_rank()[:10]
    x = np.arange(1, 11)
    y = []
    for data in datas:
        y.append(data[1])
    plt.bar(x, y)
    print(datas)
    plt.show()

def lesson37():
    print("- 「猫」と共起頻度の高い上位10語")
    datas = get_morphological_analysis_result()
    count = {}
    for data in datas:
        tmp = []
        neko_flag = False
        for val in data:
            if "猫" == val["base"]:
                neko_flag = True
            else:
                tmp.append(val["base"])
        if neko_flag:
            for t in tmp:
                if t in count:
                    count[t] = count[t]+1
                else:
                    count[t] = 1
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]
    x = np.arange(1, 11)
    y = []
    for r in result:
        y.append(r[1])
    plt.bar(x, y)
    print(result)
    plt.show()

def lesson38():
    print("- ヒストグラム -> 多分ミスってる")
    datas = get_vocaburary_rank()
    datas = [x[1] for x in datas]
    count = np.zeros(datas[0])
    for data in datas:
        count[data-1] = count[data-1]+1
    count = [int(x) for x in count]
    x = np.arange(1, len(count)+1)
    plt.plot(x, count)
    plt.show()

def lesson39():
    print("- Zipfの法則")
    datas = get_vocaburary_rank()
    datas = [x[1] for x in datas]
    count = np.zeros(datas[0])
    for data in datas:
        count[data-1] = count[data-1]+1
    count = [int(x) for x in count]
    x = np.arange(1, len(count)+1)
    plt.plot(x, count)
    ax = plt.gca()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()
    

if __name__ == "__main__":
    lesson30()
    lesson31()
    lesson32()
    lesson33()
    lesson34()
    lesson35()
    lesson36()
    lesson37()
    lesson38()
    lesson39()