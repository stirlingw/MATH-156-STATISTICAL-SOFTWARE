import glob
import os
from os.path import basename

def convert_tex_to_html():
    names = [os.path.splitext(os.path.basename(x))[0] for x in glob.glob('./personal-notes/tex-files/*.tex')]
    if len(names) > 0:
        for name in names:
            process_to_run = """pandoc ./personal-notes/tex-files/{0}.tex -s --mathjax -o ./personal-notes/html-files/{0}.html""".format(name)
            # --webtex
            # --mathjax
            print(process_to_run)
            os.system(process_to_run)
            process_to_run = None

if __name__ == '__main__':
    convert_tex_to_html()
