NAME="popular-names.txt"
echo ${NAME}

#lesson10
echo "lesson10"
echo "- 行数のカウント"
wc -l ${NAME}

#lesson11
echo "lesson11"
echo "- タブをスペースに変換"
OUTPUT="lesson11.txt"
sed "s/\t/ /g" ${NAME} | tr "\t" " " | expand -t 1 > "lesson11.txt"
# tr "\t" " " <${NAME}> "lesson11_tr.txt"
# expand -t 1 ${NAME} > "lesson11_expand.txt"

#lesson12
echo "lesson12"
echo "- 一列目をcol1.txtに、二列目をcol2.txtに保存"
cut -f -1 ${NAME} > "col1.txt"
cut -f 2-2 ${NAME} > "col2.txt"

#lesson13
echo "lesson13"
echo "- col1.txtとcol2.txtをマージ"
paste "col1.txt" "col2.txt" > "lesson13.txt"

#lesson14
echo "lesson14"
N=10
echo "- 先頭からN(${N})行を出力"
head -n ${N} ${NAME} > "lesson14.txt"

#lesson15
echo "lesson15"
echo "- 末尾からN(${N})行を出力"
tail -n ${N} ${NAME} > "lesson15.txt"

#lesson16
echo "lesson16"
echo "- ファイルをN(${N})分割する"
split -n ${N} "${NAME}"

#lesson17
echo "lesson17"
echo "- 一列目の文字列の異なり"
cut -f -1 ${NAME} | sort | uniq> "lesson17.txt"
# sort "lesson17_cut.txt" > "lesson17_sort.txt"
# uniq "lesson17_sort.txt" > "lesson17_result.txt"

#lesson18
echo "lesson18"
echo "- 各行を三コラム目の数値の降順にソート"
sort -n -k 3 ${NAME} > "lesson18.txt"

#lesson19
echo "lesson19"
echo "- 各行の一コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べる"
cut -f -1 ${NAME} | sort | uniq -c | sort -r > "lesson19.txt"  