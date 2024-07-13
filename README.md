Markdown to HTML

Start a script Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file Second argument is the output file name Requirements:

If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1 If the Markdown file doesn’t exist: print in STDER Missing and exit 1 Otherwise, print nothing and exit 0

Headings Improve markdown2html.py by parsing Headings Markdown syntax for generating HTML:
Syntax: (you can assume it will be strictly this syntax)

Markdown HTML generated

Heading level 1
Heading level 1
Heading level 2
Heading level 1
Heading level 3
Heading level 1
Heading level 4
Heading level 1
Heading level 5
Heading level 1
Heading level 6
Heading level 1
Spacing and new lines between HTML tags don’t need to be exactly this one

Unordered listing Improve markdown2html.py by parsing Unordered listing syntax for generating HTML:
Syntax: (you can assume it will be strictly this syntax)

Markdown:

Hello
Bye HTML generated:
Hello
Bye
Spacing and new lines between HTML tags don’t need to be exactly this one

Ordered listing Improve markdown2html.py by parsing Ordered listing syntax for generating HTML:
Syntax: (you can assume it will be strictly this syntax)

Markdown:

Hello
Bye HTML generated:
Hello
Bye
Spacing and new lines between HTML tags don’t need to be exactly this one

Simple text Improve markdown2html.py by parsing paragraph syntax for generating HTML:
Syntax: (you can assume it will be strictly this syntax)

Markdown:

Hello

I'm a text with 2 lines HTML generated:

Hello

I'm a text
with 2 lines

Spacing and new lines between HTML tags don’t need to be exactly this one

Bold and emphasis text Improve markdown2html.py by parsing bold syntax for generating HTML:
Syntax: (you can assume it will be strictly this syntax)

Markdown HTML generated Hello Hello Hello Hello

Spacing and new lines between HTML tags don’t need to be exactly this one

... but why?? Improve markdown2html.py by parsing bold syntax for generating HTML:
Syntax: (you can assume it will be strictly this syntax)

Markdown HTML generated description [[Hello]] 8b1a9953c4611296a827abf8c47804d7 convert in MD5 (lowercase) the content ((Hello Chicago)) Hello hiago remove all c (case insensitive) from the content

Spacing and new lines between HTML tags don’t need to be exactly this one
