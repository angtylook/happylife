#!/usr/local/bin/python3
# encoding=utf-8

import sys
import os
import pathlib

def listAllFile(dir, extension):
	for dirpath, dirname, filenames in os.walk(dir):
		for filename in filenames:
			if pathlib.Path(filename).suffix == extension:
				print(os.path.join(dirpath, filename))

if __name__ == "__main__":
	listAllFile(sys.argv[1], sys.argv[2])