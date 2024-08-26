# HTML2MD

This is a Python script designed to convert questions from an HTML file into Markdown format, facilitating their use in Markdown editors or documents.

## Features

- Parses questions from a local HTML file.
- Supports conversion for single-choice, multiple-choice, and true/false questions.
- Formats questions and options according to Markdown syntax.

## Usage

### Prerequisites

Ensure that Python 3 and the following libraries are installed on your system:

- BeautifulSoup4
- lxml or html5lib (one of them is needed as an HTML parser)

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

### Steps

- Place your HTML file in the ./examples/ directory and name it questions.html(this name is for example use).
- Ensure that your Python script and the HTML file are in the same directory.
- Run the Python script. This will generate a Markdown file named questions.md(you can name it whatever you want), saved in the ./examples/ directory.

### Example

Assuming your HTML file contains questions with the following structure:

```html
<div class="des">
  <p>题目文本</p>
  <ul>
    <li>选项 A</li>
    <li>选项 B</li>
    <!-- 更多选项 -->
  </ul>
</div>
```

After running the script, you will get a Markdown file in the following format:

```markdown
## 单选题

### 题目文本

- 选项 A
- 选项 B
<!-- 更多选项 -->
```
