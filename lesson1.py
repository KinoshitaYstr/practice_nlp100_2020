import random

def no00():
    print("- 文字列の逆順")
    s0 = "stressed"
    s1 = s0[::-1]
    print("{} -> {}".format(s0, s1))

def no01():
    print("- パタトクカシー")
    s0 = "パタトクカシー"
    s1 = ""
    for i in range(0, len(s0), 2):
        s1 = "{}{}".format(s1, s0[i])
    print(s1)

def no02():
    print("- パトカー＋タクシー＝パタトクカシー")
    s01 = "パトカー"
    s02 = "タクシー"
    s1 = ""
    for c1, c2 in zip(s01, s02):
        s1 = "{}{}{}".format(s1, c1, c2)
    print(s1)

def no03():
    print("- 円周率")
    s0 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    s0 = s0.replace(".", "")
    s0 = s0.replace(",", "")
    count = []
    for word in s0.split(" "):
        count.append(len(word))
    print(count)

def no04():
    print("- 元素記号")
    s0 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    flag = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    result = {}
    for i, word in enumerate(s0.split(" ")):
        if i+1 in flag:
            result[word] = word[0]
        else:
            result[word] = word[:2]
    print(result)

def word_n_gram(s):
    s = s.split(" ")
    result = []
    for i in range(len(s)):
        result.append([s[i], s[i+1] if i+1 < len(s) else ""])
    return result

def letter_n_gram(s):
    result = []
    for i in range(len(s)):
        result.append([s[i], s[i+1] if i+1 < len(s) else ""])
    return result

def no05():
    print("- n-gram")
    s0 = "I am an NLPer"
    print("単語bi-gram -> {}".format(word_n_gram(s0)))
    print("文字bi-gram -> {}".format(letter_n_gram(s0)))

def no06():
    print("- 集合")
    pattern1 = "paraparaparadise"
    pattern2 = "paragraph"
    X = letter_n_gram(pattern1)
    Y = letter_n_gram(pattern2)
    union = []
    intersection = []
    difference = []
    for x in X:
        for y in Y:
            if not x in union:
                union.append(x)
            if not y in union:
                union.append(y)
            if x == y and not x in intersection:
                intersection.append(x)
            if not x in Y and not x in difference:
                difference.append(x)
    print("和集合 -> {}".format(union))
    print("積集合 -> {}".format(intersection))
    print("差集合 -> {}".format(difference))

def generate_sentence(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

def no07():
    print("- テンプレートによる文生成")
    x, y, z = 12, "気温", 22.4
    print(generate_sentence(x, y, z))

def cipher(pattern):
    result = ""
    for c in pattern:
        result = "{}{}".format(result, chr(219-ord(c)) if c.islower() else c)
    return result

def no08():
    print("- 暗号文")
    pattern = "Hello, World!"
    print("{} -> {}".format(pattern, cipher(pattern)))

def no09():
    print("- Typoglycemia")
    pattern = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    result = ""
    for word in pattern.split(" "):
        if len(word) <= 4:
            r = " {}".format(word)
        else:
            r = " {}{}{}".format(word[0], "".join(random.sample(word[1:-1], len(word[1:-1]))), word[-1])
        result = "{}{}".format(result, r)
    result = result[1:]
    print(result)

if __name__ == "__main__":
    no00()
    no01()
    no02()
    no03()
    no04()
    no05()
    no06()
    no07()
    no08()
    no09()