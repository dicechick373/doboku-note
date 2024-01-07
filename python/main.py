import glob
import re
from chatGPTTextConversion.gpt3 import chat

def get_file_list(path):
    """
    ディレクトリ内のmdxファイルを取得
    """
    files =  glob.glob(f'{path}/**/*.mdx')
    return files


def convert_text(text):


    prompt = f'''
        あなたはプロのWEB記事編集者です。下記の文章の内容は変えずに、語尾をですます調に変換してください。
        必要以上に丁寧にならないように注意してください。

        出力結果は変換後のテキストのみとしてください。
        

        # 文章
        {text}
    '''
    
    # result = llm(prompt)
    result = chat(prompt)

    print(text)
    print(result)
    print('------------------')
        
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
            
            # 先頭が>の場合はそのまま出力
            if re.match('^>', s_line):
                result.append(s_line)
                continue
            
            # 先頭が!の場合はそのまま出力
            if re.match('^!', s_line):
                result.append(s_line)
                continue
            
            # 先頭が!の場合はそのまま出力
            if re.match('^（', s_line):
                result.append(s_line)
                continue
            
            # 先頭が-の場合はそのまま出力
            if re.match('^-', s_line):
                result.append(s_line)
            
            # 先頭が数字の場合はそのまま出力
            if re.match('^[0-9]', s_line):
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

    file = "pages/load/road-management/road-construction/implementation.mdx"
    
    convert(file)
        
    
