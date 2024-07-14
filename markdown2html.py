#!/usr/bin/env python3

import sys
import os
import hashlib


def convert_md5(content):
    return hashlib.md5(content.encode()).hexdigest()


def remove_c(content):
    return content.replace('c', '').replace('C', '')


def parse_markdown(file_content):
    lines = file_content.split('\n')
    html_lines = []
    in_list = False
    in_olist = False

    for line in lines:
        line = line.rstrip()

        if line.startswith('#'):
            header_level = len(line.split(' ')[0])
            header_content = line[header_level + 1:]
            html_lines.append(
                f'<h{header_level}>{header_content}</h{header_level}>'
            )

        elif line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            list_item = line[2:]
            list_item = parse_inline_formatting(list_item)
            html_lines.append(f'<li>{list_item}</li>')

        elif line.startswith('* '):
            if not in_olist:
                html_lines.append('<ol>')
                in_olist = True
            list_item = line[2:]
            list_item = parse_inline_formatting(list_item)
            html_lines.append(f'<li>{list_item}</li>')

        elif line == '':
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_olist:
                html_lines.append('</ol>')
                in_olist = False

        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            if in_olist:
                html_lines.append('</ol>')
                in_olist = False

            line = parse_inline_formatting(line)
            html_lines.append(f'<p>{line}</p>')

    if in_list:
        html_lines.append('</ul>')
    if in_olist:
        html_lines.append('</ol>')

    return '\n'.join(html_lines)


def parse_inline_formatting(text):
    text = text.replace('**', '<b>').replace('<b>', '</b>', 1)
    text = text.replace('__', '<em>').replace('<em>', '</em>', 1)
    if '[[' in text and ']]' in text:
        start = text.find('[[') + 2
        end = text.find(']]')
        content = text[start:end]
        md5_content = convert_md5(content)
        text = text.replace(f'[[{content}]]', md5_content)
    if '((' in text and '))' in text:
        start = text.find('((') + 2
        end = text.find('))')
        content = text[start:end]
        new_content = remove_c(content)
        text = text.replace(f'(({content}))', new_content)
    return text


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
        )
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as f:
        file_content = f.read()

    html_content = parse_markdown(file_content)

    with open(html_file, 'w') as f:
        f.write(html_content)

    sys.exit(0)
