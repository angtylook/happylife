#!/usr/local/bin/python3
#encoding=utf-8

import json
import csv
import argparse
import pathlib
import tempfile

def parseArgs():
    parser = argparse.ArgumentParser(description="convert csv/tab to json")
    parser.add_argument("-i", "--csv", required=True, dest="csvfile", help="path to csv/tab file")
    parser.add_argument("-o", "--json", dest="jsonfile", help="path to json file")
    parser.add_argument("-m", "--meta", dest="metafile", help="path to meta file")
    parser.add_argument("-s", "--skip", dest="skip", help="skip key with tag")
    parser.add_argument("-c", "--cfg", dest="cfg", help="only use first row as ini")
    opts = parser.parse_args()
    if opts.jsonfile == None:
        opts.jsonfile = pathlib.Path(opts.csvfile).with_suffix(".json")
    if opts.metafile == None:
        csvfile = pathlib.Path(opts.csvfile)
        metafile = pathlib.Path.joinpath(csvfile.parent, csvfile.stem).with_suffix(".meta.json")
        if pathlib.Path.exists(metafile):
            opts.metafile = metafile
    return opts

def processValue(val, d, opts):
    if "dt" not in d:
        return val
    if d["dt"] == "int":
        return int(val)
    if d["dt"] == "float":
        return float(val)
    if d["dt"] == "list<int>":
        sep = "|"
        if "sep" in d:
            sep = d["sep"]
        return [int(v) for v in val.split(sep)]
    if d["dt"] == "list<float>":
        sep = "|"
        if "sep" in d:
            sep = d["sep"]
        return [float(v) for v in val.split(sep)]
    if d["dt"] == "list<string>":
        sep = "|"
        if "sep" in d:
            sep = d["sep"]
        return val.split(sep)
    if d["dt"] == "bool":
        return int(val) > 0
    return val

def processRow(row, meta, opts):
    skips = []
    for k in row.keys():
        if k in meta:
            if opts.skip != None and "tag" in meta[k] and meta[k]["tag"] == opts.skip:
                skips.append(k)
            else:
                row[k] = processValue(row[k], meta[k], opts)
    for k in skips:
        del row[k]
    return row

def convert(opts):
    tp = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
    csvfile = open(opts.csvfile, encoding="utf-8")
    for line in csvfile:
        if line.startswith("#") or line.startswith("//"):
            continue
        tp.write(line)
    csvfile.close()
    tp.seek(0)
    reader = csv.DictReader(tp, delimiter='\t')
    meta = None
    if opts.metafile != None :
        print("use meta file: ", opts.metafile)
        meta = json.load(open(opts.metafile))
        print("meta=>\n", meta)
    data = []
    for row in reader:
        if meta != None:
            row = processRow(row, meta, opts)
        # print(row)
        data.append(row)
        # skip others use as ini file
        if opts.cfg != None:
            data = row
            break
    # print(data)
    json.dump(data, open(opts.jsonfile, mode="w", encoding='utf-8'), ensure_ascii=False, indent=2)

if __name__ == "__main__":
    opts = parseArgs()
    print(opts)
    convert(opts)

