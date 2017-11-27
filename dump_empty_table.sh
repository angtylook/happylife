#! /bin/bash
mysqldump -uroot -p -d --add-drop-table ${1} > ${2}

