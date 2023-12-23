import glob
import re
from langchain.llms import OpenAIChat
import os
from dotenv import load_dotenv
load_dotenv()
import openai
openai.api_key = os.environ['OPEN_API_KEY']

def get_file_list(path):
    """
    ディレクトリ内のmdxファイルを取得
    """
    files =  glob.glob(f'{path}/**/*.mdx')
    return files

def query_gpt_chat(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            temperature = 0,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        result = response.choices[0]["message"]["content"]
        # print(result)
    except AttributeError as e:
        error_message = f"Error: {e}"
        # print(error_message)
        result = error_message 

    
    return result



def convert_text(text):
    """
    テキストを変換
    """
    # OPEN_API_KEY = os.environ['OPEN_API_KEY']
    # llm = OpenAIChat(openai_api_key=OPEN_API_KEY ,temperature=0.0)
    

    prompt = f'''
        あなたはプロの人気ブロガーです。
        下記の文章の内容は変えずに、語尾をですます調に変換してください。
        必要以上に丁寧にならないように注意してください。
        出力結果は変換後のテキストのみとしてください。
    
        # 文章
        {text}
    '''
    
    # result = llm(prompt)
    result = query_gpt_chat(prompt)
    print(text)
    print(result)
        
    return result

def convert_file(file):
    result = []
    with open(file, encoding="utf-8") as f:
        for s_line in f:
            
            # 空白行の場合はそのまま出力
            if s_line == '\n':
                result.append(s_line)
                continue
            
            # 先頭が#の場合はそのまま出力
            if re.match('^#', s_line):
                result.append(s_line)
                continue
            
            # 先頭がQの場合はそのまま出力
            if re.match('^Q', s_line):
                result.append(s_line)
                continue
            
            
            result.append(convert_text(s_line))
    
    return result


def convert_batch(path):
    # ディレクトリを指定
    path = "pages/load/road-management"
        
    files = get_file_list(path)
    
    for i,file in enumerate(files):
        print(f'{i+1}/{len(files)} を処理中.....')
        
        # LLMを利用して変換
        result = convert_file(file)
        
        # 上書き保存
        with open(file, mode='w', encoding='utf-8') as f:
            f.write('\n'.join(result))
    
def convert(file):
    
    print(f'{file} を処理中.....')
    
    # LLMを利用して変換
    result = convert_file(file)
    
    # 上書き保存
    with open(file, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(result))
        
    

if __name__ == "__main__":
    
    file = "pages/load/road-management/road-concept/restrictions-on-private-rights.mdx"
    
    convert(file)
        
    
