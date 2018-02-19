# MATH-156-STATISTICAL-SOFTWARE
MATH - E - 156 -- Mathematical Foundations of Statistical Software class taught at Harvard.   These are my assignments, notes, personal thoughts.

## To view LaTex
- Go make an account for free at [https://www.sharelatex.com](https://www.sharelatex.com)
    - Share LaTex makes your life easier than downloading some LaTex editor.  

## LaTex Cheatsheet
- [http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html](http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html)

# Atom IDE
## To install the LaTex package on Atom IDE
- `sudo apm install latex --user`

# Pandoc
## To install Pandoc on Mac OSX
- Pandoc requires basictex or mactex
    - [https://tex.stackexchange.com/questions/307483/setting-up-basictex-homebrew](https://tex.stackexchange.com/questions/307483/setting-up-basictex-homebrew)
    - [https://ctan.org/pkg/mactex-basic](https://ctan.org/pkg/mactex-basic)
    - `brew cask install basictex`
    - `open /usr/local/Caskroom/basictex/2017.0607/`
    - Click on and install `mactex-basictex-20170607.pkg`
    - If you now try to find, say, pdflatex in the same Terminal window, it won't be in your $PATH:
        -
         ```
            $ which pdflatex
            $ pdflatex
            -bash: pdflatex: command not found
         ```

     - Open a new one, however, and you'll find it in /Library/TeX/texbin.
        - ```
            \Last login: Fri Jul 15 08:35:43 on ttys001
            \$ which pdflatex
             Library/TeX/texbin/pdflatex
          ```
- You can install pandoc using homebrew:
    - `brew install pandoc`


## To convert a LaTex .tex file to HTML
- [https://pandoc.org/demos.html}(https://pandoc.org/demos.html)
- `pandoc Problem_Set_01--Some_Fun_Integrals.tex -s --mathjax -o problem-set-01.html`

# Convert ALL LaTex .tex files to HTML
- `python3 ./personal-notes/convert_tex_to_html.py`
