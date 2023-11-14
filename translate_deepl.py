import deepl
from tqdm import tqdm
from janome.tokenizer import Tokenizer

"""
このスクリプトは、whisperにより文字起こしされた字幕をdeepl APIにより日本語に翻訳し、字幕を再生成するスクリプトである。
このコードは未完成です。
"""


def adjust_subtitle_length(subtitle, max_length=32):
    """
    字幕の長さを調整します。改行位置は形態素解析により決定されます。
    """
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(subtitle)
    current_length = 0
    new_subtitle = ""

    for token in tokens:
        token_length = len(token.surface)
        if current_length + token_length > max_length:
            new_subtitle += '\n'
            current_length = 0
        new_subtitle += token.surface
        current_length += token_length

    return new_subtitle

# API Keyを入力
API_KEY:str = input('Enter your api_key: ')

# 翻訳元のファイル名を入力
source_file:str = r'./Beyond_neural_scaling_laws_Paper_Explained_1080pFHR.srt'

# イニシャライズ
translator = deepl.Translator(API_KEY)


# srtファイルの読み込み
with open(source_file, "r") as f:
    lines = f.readlines()
# 初期化
# 新しいsrtファイルを格納するためのリスト
new_srt = []
# タイムスタンプごとに記録されている文章をピリオドまたは疑問符までで結合し、一つの文章としたものを並べたリスト
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
for s in tqdm(en_list):
    translated_sentence = translator.translate_text(s, source_lang="EN", target_lang="JA").text
    # ここで形態素解析による調整を行う
    adjusted_sentence = adjust_subtitle_length(translated_sentence)
    translated_s.append(adjusted_sentence)

print("ファイル出力中")
# 翻訳された各セグメントを、元のタイムスタンプと結合
for i in tqdm(range(len(translated_s))):
    number = lines[i*4]
    time_stamp = lines[i*4+1]
    new_srt.append(number)
    new_srt.append(time_stamp)
    new_srt.append(translated_s[i] + "\n\n")

# 新しいsrtファイルの書き込み
with open("translated_subtitle.srt", "w") as f:
    f.writelines(new_srt)