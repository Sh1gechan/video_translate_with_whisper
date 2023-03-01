# video_translate_with_whisper

このリポジトリは youtube_dl などでダウンロードした英語の動画を ffmpeg などで音声を抽出し、whisper を使った文字起こしにより作成された
srt ファイルの英語字幕をみんなの自動翻訳@TexTra API や DeepL の API を利用して翻訳するスクリプトを載せたリポジトリである。

## 必要なライブラリのインストール

`pip install -r requirements.txt`

## ffmpeg

ffmpeg をインストールしたら、以下のコマンドを CMD 等で打ち込むと動画の音声抽出ができます。\
`ffmpeg -i (抽出する動画ファイル名) -vn (抽出後の音声データ)`

## whisper

### 使い方

`whisper (音源のファイル名) --model medium --language (音源で使われている言語)`

![image](https://user-images.githubusercontent.com/76240954/215337724-60e68120-85ba-4d6e-9c9a-5de81839910e.png)
引用元：https://github.com/openai/whisper

## スクリプトについて

textra.py はみんなの翻訳@TexTra の API を用いて翻訳ができます
translate_deepl.py は DeepL API を使って翻訳ができます

## 動画の再生方法

VLC Media Player を用いて再生できます。
動画を再生させる際、VLC Media Player で srt ファイルを読みこんでください。

## TO DO

- [ ] 形態素解析などを用いて自然な字幕を作成する
