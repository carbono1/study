#-- coding:utf-8 --#

## 3-1 オブジェクトについて
"""
データとそのデータの操作を行う抽象的な固まりのことをオブジェクトと呼ぶ
pythonプログラムはオブジェクトとオブジェクトの関係を操作して処理を行う
すべてのオブジェクトは生成されてから廃棄されるまで変わらないIDというオブジェクトを識別する情報を持っている
このIDはオブジェクトの情報が格納されているメモリの場所と考えれば良い
プログラムからは、このオブジェクトへのリファレンス（変数やリテラル）を通じてオブジェクト自身を操作する
pythonの場合は、オブジェクトのリファレンスに予め方を指定する必要がない
"""

## 3-2 論理型
"""
boolという型
boolは論理値を持ち、条件文に利用できる
この論理値は、and, or, notを利用することで、変更できる
True(真)とFalse(偽)の2つの論理値がある
"""

print(True and False)
print(True and True)
print(True or False)
print(not True )
print(True and not False )

"""
and, or, notには制御のフローを変化される要素がある
"""

## 3-3 数値型
"""
int, float, complexの3つの数値型があります(論理型はintのサブクラスです)
python2系ではlongがあったが、3系で廃止されている
数値型は他の数値型と共に計算や、算術的な処理ができます
ただし、complexは一部のオペレーションを利用できません
"""

### 3-3-1 int
"""
int(整数型)は長整数で、精度の制限がない
pythonのintは精度を失わないで、かなり大きい値が持てる(現実的にはメモリに制限される)
「+」「-」をつけることで、正と負の整数を定義できる
"""
posnum = +12
negnum = -12

print(posnum, negnum)
# 16進数
print(0x11,0xff,0xffff)
# 2進数
print(0b01010)
# 8進数
print(0o12)
# 10進数を2進数、8進数、16進数に変換
print(bin(10))
print(oct(10))
print(hex(19))
# int関数は第2引数に奇数を指定できる。設定すればintに変換できる
print(int('a', 16))
print(int('z', 36))
print(int('py', 36))

## 3-3-3 complex(複素数型)
"""
complex(複素数型)は実数と虚数を含む複素数を表現できます。
実数と虚数は浮動小数点です
実数はrealというプロパティでアクセスでき、虚数はimageというプロパティでアクセスできます。
実数の虚数は下記の数式を表現します

a +bi
"""

## 3-3-4 mathモジュール
import math
print(math.pi)

## 3-3-5 cmathモジュール
"""
complexの演算を行う関数を提供する
"""

## 3-3-6 nubersモジュール
"""
数値型の抽象的ベースクラスを定義している
このクラスは数値型のオブジェクトのプロパティと演算を定義する
"""
import numbers
obj = 1
print(isinstance(obj, numbers.Real))

## 3-4 シーケンス
"""
シーケンスはオブジェクトをシーケンシャル(順番)に処理するためのデータ構造です
コンテナ、イテレータ、ジェネレータといった種類がある
"""

### 3-4-1 文字列/バイト列
"""
pythonの文字列型はstrです
strは内部でunicodeデータを保持します
strは復号化されたテキストとして使います
スクリプトファイル中のテキスト文字列はファイルのエンコーディングに従って、strオブジェクトをunicodeに変換します
python2ではasciiを想定していたが、python3ではutf-8を想定している
ファイルの文字コードの設定の仕方はPEP263で定義されている

符号化されたテキストデータを扱うにはbytes型を使う
bytesは単のバイナリデータの列ですが、テキストデータを扱う際に便利な演算ができます
bytes型は「b」文字をテキストの先頭につける
"""
print(b"there are some bytes.")

"""
bytesのテキストはascii文字種で書かないといけない
かけない場合は、\\x付けてエスケープする
その後の文字はバイト値の16進数の文字になる
コンストラクタやencodeとdecodeメソッドで、bytesとstrのテキストは符号化したり復号化したりできる
"""

x = 'テスト'.encode()
print(x.decode())

x = '高岡'.encode('utf-8')
print(x.decode('utf-8'))

"""
ucs2とucs4
PEP393
3.2までは、どっちでコンパイルするかによってunicodeの文字列長が異なるという話
3.3では裏側の構造体で吸収されたのでどちらでも結果が同じになるようになった
"""
import sys
print(sys.maxunicode)

#### イミュータブル
"""
str型とbytes方は共にイミュータブル(変更不要)オブジェクトです
イミュータブルとはオブジェクト自身の状態を変更できない性質のものです
変数に割り当てているイミュータブルなオブジェクトの状態を変える場合は、
新しいオブジェクトを生成して変数の指し示す先を新しいオブジェクトに変える
"""

"""
idという関数は、オブジェクトの固有番号を返す関数
cpythonの場合は、ポインタ(メモリの位置)を返します
"""
s = 'spam'
print(id(s))
s = 'egg'
print(id(s))

### column
a = 'spam'
b = 'spam'
c = 'spam'
print(id(a), id(b), id(c))
print('spam'.lower() is 'spam'.lower())
print(sys.intern('spam'.lower()) is sys.intern('spam'.lower()))

### 3-4-2 バイト配列型
"""
bytes型はイミュータブルで要素の変更ができないが、bytearray(バイト配列型)はミュータブル
ミュータブルであることの他はbytes型と同じ機能を持っている
bytearrayはbytearrayコンストラクタで生成します
要素1つ1つは0から255までの数値です
"""

ba1 = bytearray()
ba1.append(115)
ba1.append(112)
ba1.append(97)
ba1.append(109)
print(ba1)

ba2 = bytearray([115,112,97,109])
print(ba2)
ba2[3] = 111
print(ba2)

ba3 = bytearray('スパム', 'utf-8')
print(ba3)
print(len(ba3))
print(ba3.decode())

ba4 = bytearray(b'egg')
print(ba4)

ba5 = bytearray(128)
print(ba5)

### 3-4-3 リスト
"""
順序を保ちながらオブジェクトをリストする場合、list型を使う
list型はビルトイン型で、種類を問わずオブジェクトを格納できる
多次元リストを表現するためにlistにlistを格納することもできる
pythonのlistは格納する型の定義が必要ない
list型はミュータブル(変更可能)
"""

x = [1,2,3.0,"a","b","c"]
print(x)
print('listの0番目', x[0])
print('listの6番目', x[5])
print('listの6番目', x[-1])

"""
pythonのシーケンス番号も0始まり
"""

#### スライス
"""
スライスというのは、listからサブリストを得るためのシンタックス
間違った順序を指定すると空のlistが返ってくるのが注意点
"""
print(x[0:2])
print(x[:-2])
print(x[2:-2])
print(x[2:])

#### イテレーション
"""
listに対する処理でよく使うのは、リストないの全要素に対して
順に何らかの処理をすること
"""
for item in x:
    print(item)

x = ['ab','test']

for i in x[0]:
    print(i)

#### リストの更新
y = []
y.append('test')
print(y)
y.append('あきと')
print(y)
y.append(100)
print(y)
y.remove(100)
print(y)
y[1] = 100
print(y)

x = [1,2,3,4,5]
print(x)
print(x[1:4])
x[1:4] = ["spam", "test"]
print(x)

"""
reverseメソッドはlist自体の並び替えを行うため、新しいコピーができないことに注意
"""
x = [1,2,3]
print(x)
x.reverse()
print(x)

"""
sortのアルゴリズムはTimeSortを使用している
"""
x = [1,3,6,2,4,0,8,7]
print(x)
x.sort()
print(x)

#### リスト内包表記(リストコンプリヘンション)
"""
リスト内包表記はループと条件を使って新しいlistを生成する特別なシンタックス
"""
print([i for i in range(10) if i % 2 == 0])

### 3-4-4 タプル
"""
listと別のシーケンス型
listと異なり、イミュータブル(不変)
格納する値の型が自由であることはlistと同様
tupleもインデックスで要素を取り出せるが、tupleへの要素の割り当てはサポートされていない
"""
x = (1,2,3,"a","b","c")
print(x[0])
y = (1)
print(type(y))
y = (1,)
print(type(y))

"""
tupleの利点
スピードが少しだけ速い
イミュータブルなので、ハッシュ化可能で辞書型のキーに利用できる
"""
