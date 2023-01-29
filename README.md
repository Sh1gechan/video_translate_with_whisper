# video_translate_with_whisper
このリポジトリはyoutube_dlなどでダウンロードした英語の動画をffmpegなどで音声を抽出し、whisperを使った文字起こしにより作成された
srtファイルの英語字幕をみんなの自動翻訳@TexTra APIやDeepLのAPIを利用して翻訳するスクリプトを載せたリポジトリである。

## whisper

### インストール
```pip install git+https://github.com/openai/whisper.git```

### 使い方
```whisper (音源のファイル名) --model medium --language (音源で使われている言語)```

![image](https://user-images.githubusercontent.com/76240954/215337724-60e68120-85ba-4d6e-9c9a-5de81839910e.png)
引用元：https://github.com/openai/whisper


## TO DO
DeepL翻訳に合わせたスクリプトを書く
