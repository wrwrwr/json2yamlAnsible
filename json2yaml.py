#!/usr/local/bin/python

import re, sys, json, yaml

with open(sys.argv[1]) as f:
#   print yaml.safe_dump(json.load(f), default_flow_style=False)
   a = yaml.safe_dump(json.load(f), default_flow_style=False)

c = sys.argv[1] + ".yml"

text_file = open(c, "w")
text_file.write(a)
text_file.close

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
    'IpProtocol:': '          - proto:',
    '- Description:': '        description:',
    'SecurityGroups:': '- name:',
    '  IpPermissions:': '        rules:',
    '  IpPermissionsEgress:': '        rules_egress:'
}


replacements = dict((re.escape(k), v) for k, v in replacements.iteritems())
pattern = re.compile('|'.join(replacements.keys()))


def replace(text):
    return pattern.sub(lambda m: replacements[re.escape(m.group(0))], text)


with open(c, 'rt') as fin:
    with open(c + ".out", 'wt') as fout:
#    with open(c + ".out", 'wt') as fout:
        for line in fin:
            fout.write(replace(line))
