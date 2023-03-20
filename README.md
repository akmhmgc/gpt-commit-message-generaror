# Gitコミットメッセージ自動生成スクリプト

このスクリプトは、GPT-3を使用して適切なGitコミットメッセージを自動生成するためのツールです。`git diff`の出力を基に、英語でコミットメッセージを提案します。

# 事前準備
1. Python 3.6以上をインストールしてください。
2. OpenAIのPythonパッケージをインストールします。

```bash
pip install openai
```

# スクリプトの設定
1. 環境変数で`OPEN_API_KEY`を指定してください。

2. ターミナルで、スクリプトに実行権限を付与します。

```bash
$ chmod +x generate_commit_message.py
```

# 使用方法
1. ターミナルで、以下のコマンドを実行してスクリプトを起動します。

```bash
$ ./generate_commit_message.py
```

2. スクリプトが実行されると、`git diff --staged`の出力をもとに、GPT-3が自動生成したコミットメッセージが表示されます。

3. 表示されたコミットメッセージを使用して、通常通りgit commitコマンドを実行してください。

これで、GPT-3によって生成された適切なコミットメッセージを使用して、コミットが行われます。スクリプトは何度でも実行できますので、コミットメッセージの生成が必要な度にお使いいただけます。

# bashなどのエイリアスとして登録する方法

1. スクリプト（`generate_commit_message.py`）を適当な場所に置きます。例えば、ホームディレクトリの直下にscriptsディレクトリを作成して、そこにスクリプトを置くことができます。

```sh
mkdir -p ~/scripts
mv generate_commit_message.py ~/scripts/
```

2. エイリアスを設定するために、`.bashrc`ファイル（bashの場合）または.`zshrc`ファイル（zshの場合）を編集します。エディタを使って該当のファイルを開いてください。例えば、`nano`を使って編集する場合は以下のようになります。

```sh
nano ~/.bashrc  # bashの場合
# または
nano ~/.zshrc   # zshの場合
```

3. 設定ファイルの最後に、以下の行を追加します。`/path/to/your/scripts`は、スクリプトを置いたディレクトリのパスに置き換えてください。

```sh
alias generate_commit_message="/path/to/your/scripts/generate_commit_message.py"
```

例:
```sh
alias generate_commit_message="$HOME/scripts/generate_commit_message.py"
```

4. 設定ファイルを保存し、閉じます。

5. 変更を反映させるために、以下のコマンドを実行して、設定ファイルを再読み込みします。

```sh
source ~/.bashrc  # bashの場合
# または
source ~/.zshrc   # zshの場合
```
