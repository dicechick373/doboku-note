import glob
import re
from chatGPTTextConversion.gpt4 import chat

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
        文章に"道路法第◯条"や,"高速自動車国道法第◯条"、"道路交通法第◯条"という表現がある場合は、Markdownリンクに変換してください。すでにMarkdownリンクになっている場合はそのままにしてください。
        出力結果は変換後のテキストのみとしてください。
        
        例の入力：
         - "道路法第15条によれば、運転者は信号に従う必要があります。速度制限に関するのは道路法第30条です。"
         - "高速自動車国道法第23条に基づき、国土交通大臣が行う道路に関する調査があります。"
         - "道路交通法第1条によれば"
         - "施行令第4条第 1 項 14 号の規定により、"
         - "様式については施行規則 5Ⅲ 参照"
         - "港湾法 2 条 Ⅱ"
         - "国賠法第2条"
         
        期待される出力:
         - "道路法第15条によれば、運転者は信号に従う必要があります。速度制限に関するのは[道路法第30条](https://elaws.e-gov.go.jp/document?lawid=327AC1000000180#Mp-At_30)です。"
         - "[高速自動車国道法第23条](https://elaws.e-gov.go.jp/document?lawid=332AC0000000079#Mp-At_23)に基づき、国土交通大臣が行う道路に関する調査があります。"
         - "[道路交通法第1条](https://elaws.e-gov.go.jp/document?lawid=335AC0000000105#Mp-At_1)によれば"
         - "[施行令第4条](https://elaws.e-gov.go.jp/document?lawid=327CO0000000479_20230401_504CO0000000378#Mp-At_4)第 1 項 14 号の規定により、"
         - "様式については[道路法施行規則第5条](https://elaws.e-gov.go.jp/document?lawid=327M50004000025#Mp-At_5)第3項参照"
         - "[港湾法第2条](https://elaws.e-gov.go.jp/document?lawid=325AC0000000218#Mp-At_2)第2項"
         - "[国家賠償法第2条](https://elaws.e-gov.go.jp/document?lawid=322AC0000000125_20150801_000000000000000#Mp-At_2)"
         
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
    
    file = "pages/load/road-management/road-construction/power.mdx"
    
    convert(file)
        
    
