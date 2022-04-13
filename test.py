
import pylatexenc.latex2text

FILE_NAME = '/home/wenjie/work/research-compiling-error-fixing/OOPSLA-2022-2/chaps/04-approach.tex'

with open(FILE_NAME, 'r') as f:
    text = f.read()

converter = pylatexenc.latex2text.LatexNodes2Text(math_mode='remove', keep_comments=False, strict_latex_spaces=False, fill_text=False)
text_tuples = converter.latex_to_text_tuples(text)

print(text_tuples)