pandoc -N -s --toc -f markdown+smart --pdf-engine=xelatex --highlight-style kate -V CJKmainfont="ËÎÌו" -V mainfont=Consolas -V geometry:margin=1in ${1} -o ${2}

