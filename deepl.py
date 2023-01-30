import re
import deepl
from tqdm import tqdm



# API Keyを入力
API_KEY:str = input('Enter your api_key: ')

# 翻訳元のファイル名を入力
source_file:str = r'./Deep_Ensembles_A_Loss_Landscape_Perspective.srt'



# イニシャライズ
translator = deepl.Translator(API_KEY)


# # srtファイルの読み込み
# with open(source_file, "r") as f:
#     lines = f.readlines()
# # 新しいsrtファイルを格納するためのリスト
# new_srt = []


# # 各行に対して処理
# for i in tqdm(range(0, len(lines), 4)):
#     # 時間の設定
#     time = lines[i+1]
#     # 字幕の文章を結合
#     sentence = lines[i+2]
#     j = i + 2
#     end_of_sentence = False
#     while not end_of_sentence:
#         if lines[j].endswith("."):
#             sentence += lines[j]
#             end_of_sentence = True
#         elif j == len(lines) - 1:
#             sentence += lines[j]
#             end_of_sentence = True
#         else:
#             sentence += lines[j]
#             j += 1
#     # 翻訳
#     translated_sentence = translator.translate_text(sentence, source_lang="EN", target_lang="JA")
#     # 文章の長さの分割
#     sentences = split_sentences(translated_sentence.text)
#     for s in sentences:
#         new_srt.append(time)
#         new_srt.append(s + "\n")
#         new_srt.append("\n")


"""
このスクリプトは、whisperにより文字起こしされた字幕をみんなの自動翻訳@deepl APIにより日本語に翻訳し、字幕を再生成するスクリプトである。
このコードは未完成です。
"""
# TO DO 
# DeepL翻訳に対応させたスクリプトに書き換える

name = input('Enter your name: ')
api_key = input('Enter your api_key: ')
api_secret = input('Enter your secret: ')
url = input('Enter your url: ')

source_file:str = r'./Deep_Ensembles_A_Loss_Landscape_Perspective.srt'

# srtファイルの読み込み
with open(source_file, "r") as f:
    lines = f.readlines()
# 初期化
# 新しいsrtファイルを格納するためのリスト
new_srt = []
# タイムスタンプごとに記録されている文章を
# ピリオドまたは疑問符までで結合し、
# 一つの文章としたものを並べたリスト
en_list = []
# en_listにappendするための変数
temp = ""
# タイムスタンプごとの文章を記録したリスト
sentence_list = []
# 文字数をカウントするためのリスト
word_count = []
# 文章の割合を保存するリスト
ratio = []
# ratioの集まりをあらわすリスト
ratio_list = []

print("前処理")
for i in tqdm(range(0, len(lines), 4)):
    sentence = lines[i+2]
    sentence_list.append(lines[i+2])

    
    # 一文一文を結合し、リストに保存
    if "." in sentence or "?" in sentence or "!" in sentence:
        temp += sentence.replace('\n', ' ')
        en_list.append(temp)
        temp = ""
        word_count.append(len(sentence))
        for count in word_count:
            ratio.append(count/sum(word_count))
        ratio_list.append(ratio)
        ratio = []
        word_count = []
    else:
        temp += sentence.replace('\n', ' ')
        word_count.append(len(sentence))



# 結合された文章の長さを保存するリスト
en_list_length = [len(s) for s in en_list]
# タイムスタンプごとの文章の長さのリスト
sentence_list_length = [len(l) for l in sentence_list]

print("翻訳中")
translated_s = []
# 翻訳を行う部分
for i, s in tqdm(enumerate(en_list)):
    translated_sentence = translator.translate_text(s, source_lang="EN", target_lang="JA")
    translated_s.append(translated_sentence)
    # data = {
    #     'key': api_key,
    #     'name': name,
    #     'type': 'json',
    #     'text': s,
    #     'split': '0',
    # }
    # result = requests.post(url, data=data, auth=OAuth1(api_key, api_secret)).json()
    # translated_s.append(result['resultset']['result']['text'])

print("ファイル出力中")
# 翻訳後の文章をsplitしてタイムスタンプの後ろに挿入するためのリスト
split_translated_s = []
for i in range(len(translated_s)):
    start = 0 #開始位置の設定
    for j in range(len(ratio_list[i])):
        length = int(len(translated_s[i]) * ratio_list[i][j]) # 割合を取り出す, 割合に従って長さを決める
        split_translated_s.append(translated_s[i][start:start+length]) # 分割した文章を追加
        start += length


for i in tqdm(range(len(split_translated_s))):
    #番号の設定
    number = lines[i*4]
    # タイムスタンプの設定
    time_stamp = lines[i*4+1]
    new_srt.append(number)
    new_srt.append(time_stamp)
    # ratioからとりだした割合をかけ、タイムスタンプの後ろに挿入
    new_srt.append(split_translated_s[i])
    new_srt.append("\n")
    new_srt.append("\n")
   
# 新しいsrtファイルの書き込み
with open("translated_subtitle.srt", "w") as f:
    f.writelines(new_srt)
