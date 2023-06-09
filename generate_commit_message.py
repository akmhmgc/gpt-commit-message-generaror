#!/usr/bin/env python3

import openai
import os
import sys
import subprocess

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

# APIキーが設定されていない場合は、ユーザーに入力を促す
if api_key is None:
    api_key = input("Please enter your OpenAI API key: ")

# APIキーを設定
openai.api_key = api_key

# git diff --stagedの出力を取得
git_diff = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
diff_output = git_diff.stdout

# GPT-3へのリクエストを作成
prompt = f"Given the following git diff output, suggest an appropriate commit message in English:\n\n{diff_output}\n\nCommit message:"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
)

# コミットメッセージを取得して表示
commit_message = response.choices[0].text.strip()
print(commit_message)
