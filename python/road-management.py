import glob

if __name__ == "__main__":
    
    # ディレクトリを指定
    path = "pages/load/road-management"
    
    # ディレクトリ内のmdxファイルを取得
    files =  glob.glob(f'{path}/**/*.mdx')

    for file in files:
        with open(file, encoding="utf-8") as f:
            for s_line in f:
                
                # 法
                print(s_line)
    
