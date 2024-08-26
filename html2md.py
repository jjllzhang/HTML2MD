from bs4 import BeautifulSoup
import re

HTML_FILE = './examples/questions.html' # 本地HTML文件路径
MARKDOWN_FILE = './examples/questions.md' # 将要保存的MD文件路径

# 读取本地HTML文件
with open(HTML_FILE, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 创建Markdown文件并写入转换后的内容
with open(MARKDOWN_FILE, 'w', encoding='utf-8') as md_file:
    # 找到所有的题目描述部分，包括单选题和判断题
    questions = soup.find_all(['div', 'class'], [('des',), ('des_2',)])

    # 遍历每个问题，提取内容并转换为Markdown格式
    for (index, question) in enumerate(questions, start=1):  
        # 根据类名判断题目类型
        if question.get('class')[0] == 'des':
            # 单选题或多选题
            if index == 1:
                md_file.write("## 单选题\n")
            elif index == 41:
                md_file.write("## 多选题\n")
            # 提取题目文本
            question_text = question.find('p').text.strip()
            # 写入题目到Markdown文件
            md_file.write(f"### {question_text}\n\n")

            # 提取选项列表
            options = question.find_all('li')
            # 遍历选项并转换为Markdown格式
            for _, option in enumerate(options, start=1):
                # 提取选项文本
                option_text = option.text.strip()
                option_text = re.sub(r'\.(\s*)', '.  ', option_text)
                # 检查是否有正确答案的提示
                correct_answer = option.find('input', {'class': 'cw'})
                if correct_answer:
                    correct_answer_text = correct_answer['value']
                else:
                    correct_answer_text = ''
                # 构建Markdown格式的选项
                option_md = f"{option_text}"
                if correct_answer_text:
                    option_md += f" **{correct_answer_text}**"
                    option_md = "\n" + option_md
                # 写入选项到Markdown文件
                md_file.write(f"{option_md}\n")
        elif question.get('class')[0] == 'des_2':
            # 判断题
            if index == 61:
                md_file.write("## 判断题\n")
            # 提取题目文本
            question_text = question.find('p').text.strip()
            # 写入题目到Markdown文件
            md_file.write(f"### {question_text}\n\n")

            # 检查是否有正确答案的提示
            # correct_answer = question.find('input', {'class': 'cw'})['value']
            if question.find('input', {'class': 'cw'})['value'] == "T":
                correct_answer = "正确"
            else:
                correct_answer = "错误"


            # 构建Markdown格式的判断题选项
            true_false_md = f"- 正确  \n- 错误 \n"
            answer_md = f"答案: **{correct_answer}**"

            # 写入选项到Markdown文件
            md_file.write(f"{true_false_md}\n")
            md_file.write(f"{answer_md}\n")

        # 每个题目后面添加一个空行
        md_file.write("\n")