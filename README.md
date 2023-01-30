# video_translate_with_whisper
このリポジトリはyoutube_dlなどでダウンロードした英語の動画をffmpegなどで音声を抽出し、whisperを使った文字起こしにより作成された
srtファイルの英語字幕をみんなの自動翻訳@TexTra APIやDeepLのAPIを利用して翻訳するスクリプトを載せたリポジトリである。

## 必要なライブラリのインストール
```pip install -r requirements.txt```

## ffmpeg
ffmpegをインストールしたら、以下のコマンドをCMD等で打ち込むと動画の音声抽出ができます。\
```ffmpeg -i (抽出する動画ファイル名) -vn (抽出後の音声データ)```

## whisper

### インストール
```pip install git+https://github.com/openai/whisper.git```

### 使い方
```whisper (音源のファイル名) --model medium --language (音源で使われている言語)```

![image](https://user-images.githubusercontent.com/76240954/215337724-60e68120-85ba-4d6e-9c9a-5de81839910e.png)
引用元：https://github.com/openai/whisper

## スクリプトについて
textra.pyはみんなの翻訳@TexTraのAPIを用いて翻訳ができます
translate_deepl.pyはDeepL APIを使って翻訳ができます

## 動画の再生方法
VLC Media Playerを用いて再生できます。
動画を再生させる際、VLC Media Playerでsrtファイルを読みこんでください。

## TO DO
- [ ] DeepL翻訳に合わせたスクリプトを書く
- [ ] 形態素解析などを用いて自然な字幕を作成する
