import json
from json.decoder import WHITESPACE
import requests

def lesosn20():
    print("- JSONデータの読み込み")
    p = "../jawiki-country.json"
    articles = []
    with open(p, "r") as f:
        for line in f.readlines():
            d = json.loads(line)
            articles.append(d)
    for article in articles:
        if article["title"] == "イギリス":
            data = article["text"]
            break
    print(data)

def get_data():
    p = "../jawiki-country.json"
    articles = []
    with open(p, "r") as f:
        for line in f.readlines():
            d = json.loads(line)
            articles.append(d)
    for article in articles:
        if article["title"] == "イギリス":
            data = article["text"]
            break
    return data

def lesosn21():
    print("- カテゴリ名を含む行を抽出")
    data = get_data()
    for line in data.split("\n"):
        if "[[Category" in line:
            print(line)

def lesosn22():
    print("- カテゴリ名の抽出")
    data = get_data()
    for line in data.split("\n"):
        if "[[Category" in line:
            print(line.replace("[[Category:", "").replace("]]", ""))

def lesosn23():
    print("- セクション構造")
    section_num = 1
    data = get_data()
    for line in data.split("\n"):
        if "====" in line:
            print(" - - {} {}".format(sub_sub_section_num, line.replace("=", "")))
            sub_sub_section_num += 1
        elif "===" in line:
            print(" - {} {}".format(sub_section_num, line.replace("=", "")))
            sub_section_num += 1
            sub_sub_section_num = 1
        elif "==" in line:
            print(section_num, line.replace("=", ""))
            section_num += 1
            sub_section_num = 1

def lesosn24():
    print("- ファイル参照の抽出")
    data = get_data()
    for line in data.split("\n"):
        if "ファイル" in line:
            if line.index("[[ファイル") != 0:
                # print(line)
                line = line[line.index("[[ファイル"):]
            start_i = line.index(":")+1
            end_i = line.index("|") if "|" in line else line.index("]]")
            print(line[start_i:end_i])

def lesosn25():
    print("- テンプレートの抽出")
    data = get_data()
    templates = {}
    flag = False
    for line in data.split("\n"):
        if '{{基礎情報' in line:
            flag = True
        elif flag and " = " in line:
            line = line[1:].split(" = ")
            templates[line[0]] = line[1]
    print(templates)

def get_templates():
    data = get_data()
    templates = {}
    flag = False
    for line in data.split("\n"):
        if '{{基礎情報' in line:
            flag = True
        elif flag and " = " in line:
            line = line[1:].split(" = ")
            templates[line[0]] = line[1]
    return templates

def lesosn26():
    print("- 強調マークアップの除去")
    templates = get_templates()
    for k, t in templates.items():
        templates[k] = t.replace("'", "")
    print(templates)

def get_templates_remove_emphasis():
    templates = get_templates()
    for k, t in templates.items():
        templates[k] = t.replace("'", "")
    return templates

def lesosn27():
    print("- 内部リンクの除去")
    templates = get_templates_remove_emphasis()
    for k, t in templates.items():
        if "[[" in t:
            t = t.replace("[", "").replace("]", "")
            templates[k] = t
    print(templates)

def get_templates_remove_emphasis_and_internal_link():
    templates = get_templates_remove_emphasis()
    for k, t in templates.items():
        if "[[" in t:
            t = t.replace("[", "").replace("]", "")
            templates[k] = t
    return templates

def lesosn28():
    print("- mediawikiマークアップの除去")
    templates = get_templates_remove_emphasis_and_internal_link()
    for k, t in templates.items():
        t = t.replace("*", '').replace('[', '').replace(']', '').replace('=', '').replace('#', '').replace('"', '').replace(';', '')
        templates[k] = t
    print(templates)

def get_templates_remove_markdown():
    templates = get_templates_remove_emphasis_and_internal_link()
    for k, t in templates.items():
        t = t.replace("*", '').replace('[', '').replace(']', '').replace('=', '').replace('#', '').replace('"', '').replace(';', '')
        templates[k] = t
    return templates

def lesosn29():
    print("- 国旗画像のURLを取得する")
    templates = get_templates_remove_markdown()
    s = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    prm = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:{}".format(templates["国旗画像"])
    }
    r = s.get(url=URL, params=prm)
    data = r.json()
    pages = data["query"]["pages"]
    for k, v in pages.items():
        print("{} is uploaded by User:{}".format(v["title"], v["imageinfo"][0]["user"]))

if __name__ == "__main__":
    lesosn20()
    lesosn21()
    lesosn22()
    lesosn23()
    lesosn24()
    lesosn25()
    lesosn26()
    lesosn27()
    lesosn28()
    lesosn29()