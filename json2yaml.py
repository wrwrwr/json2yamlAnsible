#!/usr/bin/env python

import json
import os
import re
import sys

import yaml

replacements = {
    '    ToPort:': '            to_port:',
    '  - FromPort:': '            from_port:',
    'UserIdGroupPairs:': '',
    'Vpc:': '',
    'VpcPeeringConnectionId:': '',
    'UserIdGroupPairs:': '',
    'PrefixListIds: []': '',
    '- Description:': '        description:',
    '  GroupName:': '    - name:',
    '  -     IpProtocol:': '          - proto:',
    '- Description:': '        description:',
    'SecurityGroups:': '- name:',
    '  IpPermissions:': '        rules:',
    '  IpPermissionsEgress:': '        rules_egress:',
    '  GroupId:': '',
    '    - GroupId:': '            group_id:',

    '~~~NO_SUCH_KEY~~~': None  # Empty remove pattern would match every line.
}
replacements = dict((re.escape(k), v) for k, v in replacements.iteritems())
remove_pattern = re.compile('|'.join(
        k for k, v in replacements.iteritems() if v is None))
replace_pattern = re.compile('|'.join(
        k for k, v in replacements.iteritems() if v is not None))


def rewrite(line):
    if remove_pattern.search(line):
        return ''
    return replace_pattern.sub(
                lambda m: replacements[re.escape(m.group())], line)

filename = sys.argv[1]
with open(filename) as fin:
    text = yaml.safe_dump(json.load(fin), default_flow_style=False)
with open(os.path.splitext(filename)[0] + '.yml', 'w') as fout:
    for line in text.splitlines():
        fout.write(rewrite(line) + os.linesep)
