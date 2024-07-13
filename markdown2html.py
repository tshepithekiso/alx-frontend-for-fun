#!/usr/bin/python3
"""
Script markdown2html.py that takes an argument 2 strings
and converts a Markdown file to HTML
"""
import sys
import os
from markdown import markdown


if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

with open(markdown_file, 'r') as f:
    markdown_content = f.read()

html_content = markdown(markdown_content)

with open(html_file, 'w') as f:
    f.write(html_content)

sys.exit(0)
