#!/usr/local/bin/python

import re, sys

ymlfile = sys.argv[1]

replacements = {
    'ToPort': 'to_port',
    'FromPort': 'from_port',
    'UserIdGroupPairs:': ''
}
replacements = dict((re.escape(k), v) for k, v in replacements.iteritems())
pattern = re.compile('|'.join(replacements.keys()))


def replace(text):
    return pattern.sub(lambda m: replacements[re.escape(m.group(0))], text)


with open(ymlfile, 'rt') as fin:
    with open('out.txt', 'wt') as fout:
        for line in fin:
            fout.write(replace(line))