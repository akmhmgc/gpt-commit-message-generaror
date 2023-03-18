#!/bin/bash

# GPT-3 APIキーを環境変数に設定
export OPENAI_API_KEY="your_api_key_here"

# git diffの出力をファイルに保存
git diff --staged > diff_output.txt

# Pythonスクリプトを実行してコミットメッセージを生成
python3 generate_commit_message.py

# 一時ファイルを削除
rm diff_output.txt
