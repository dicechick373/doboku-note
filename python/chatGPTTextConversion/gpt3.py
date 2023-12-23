import openai
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAIのAPIキーを設定
openai.api_key = os.environ['OPEN_API_KEY']

# 使用するGPTモデルの指定
model = "gpt-3.5-turbo-1106"

def chat(prompt):
    """
    GPT-4モデルを使用してチャットの応答を生成する関数。

    Args:
        prompt (str): ユーザーからの入力プロンプト。

    Returns:
        str: GPT-4モデルによって生成されたチャットの応答。
    """
    try:
        # OpenAI ChatCompletion APIを使用してチャットの応答を取得
        response = openai.ChatCompletion.create(
            model=model,
            temperature=0,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        
        # 応答から最初の選択肢のメッセージコンテンツを取得
        result = response.choices[0]["message"]["content"]
    except AttributeError as e:
        # エラーが発生した場合はエラーメッセージを表示
        error_message = f"Error: {e}"
        result = error_message

    # 生成されたチャットの応答を返す
    return result


