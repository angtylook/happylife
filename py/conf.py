#!/usr/bin/env python3

'''
'''

import argparse
import os
import configparser

def ReadArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--dir", help="work directory", default=os.getcwd())
	parser.add_argument("-r", "--region", help="region")
	parser.add_argument("-e", "--env", help="env", default="test")
	parser.add_argument("-f", "--file", help="file", default="env.ini")
	parser.add_argument("-s", "--section", help="section", default="env")
	parser.add_argument("-c", "--clear", help="clear key", action="store_true")
	parser.add_argument("key", help="key to modify")
	parser.add_argument("value", help="value to set")
	args = parser.parse_args()
	return args

def HandleRegion(args, region):
	print("handle region {}".format(region))
	if args.env != None:
		HandleEnv(args, region, args.env)
	else:
		currenRegion = os.path.join(args.dir, region)
		for file in os.listdir(currenRegion):
			if os.path.isdir(os.path.join(currenRegion, file)):
				HandleEnv(args, region, file)

def HandleEnv(args, region, env):
	cfgFile = os.path.join(args.dir, region, env, args.file)
	print("handle file {}".format(cfgFile))
	config = configparser.ConfigParser()
	config.optionxform = lambda option: option
	config.read(cfgFile, encoding="utf-8")
	if args.clear:
		if not config.has_section(args.section):
			return
		if not config.has_option(args.section, args.key):
			return
		config.remove_option(args.section, args.key)
		with open(cfgFile, 'w', encoding="utf-8") as configfile:
			config.write(configfile, space_around_delimiters=False)
		return
	if not config.has_section(args.section):
		config.add_section(args.section)
	config.set(args.section, args.key, args.value)
	with open(cfgFile, 'w', encoding="utf-8") as configfile:
		config.write(configfile, space_around_delimiters=False)


if __name__ == '__main__':
	args = ReadArgs()
	print(args)
	if args.region != None:
		HandleRegion(args, args.region)
	else:
		for file in os.listdir(args.dir):
			if os.path.isdir(os.path.join(args.dir,file)):
				HandleRegion(args, file)