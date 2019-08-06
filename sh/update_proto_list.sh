tmp=$(mktemp)
py -3 list_all.py . .proto > ${tmp}
sed 's/\.\\/clang-format -style=file -i /' ${tmp} > format_all_proto.bat
