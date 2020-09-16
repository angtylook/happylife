pandoc -N -s --toc -f markdown+smart --pdf-engine=xelatex --highlight-style kate -V CJKmainfont="宋体" -V mainfont=Consolas -V geometry:margin=1in ${1} -o ${2}

