#!/usr/local/bin/python

import sys, json, yaml, re, fileinput, subprocess, os

bad_words = ['', '']

with open(sys.argv[1]) as f:
#   print yaml.safe_dump(json.load(f), default_flow_style=False)
   a = yaml.safe_dump(json.load(f), default_flow_style=False)

#print a

b = sys.argv[1]

c = sys.argv[1] + ".yml"

text_file = open(c, "w")
text_file.write(a)
text_file.close

command = ["sed", "-i", "'/VpcPeeringConnectionId/d;/PrefixListIds/d;/PeeringStatus/d;/UserIdGroupPairs/d'", b + ".yml" ]
command2 = ["awk", "!/Vpc|IdGroup|VpcPeeringConnectionId|PrefixListIds|PeeringStatus/", c, ">", "temp", "&&", "mv", "temp", c ]

#sed '/VpcPeeringConnectionId/d;/PrefixListIds/d;/PeeringStatus/d' sg-a54f3cde.json.yml      #to test output
#sed -i '/VpcPeeringConnectionId/d;/PrefixListIds/d;/PeeringStatus/d' sys.argv[1].yml   #to make the file change
#subprocess.Popen([ 'sed', '-i', '/VpcPeeringConnectionId/d;/PrefixListIds/d;/PeeringStatus/d', b + '.yml'])

output,error  = subprocess.Popen(
                    command2, universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()


with open(c, "rt") as fin:
    with open("out.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('ToPort', 'to_port').replace('FromPort', 'from_port').replace('UserIdGroupPairs: []', ''))
#        for line in fin:
#            fout.write(line.replace('FromPort', 'from_port'))
#            fout.write(line.replace('GroupId', 'group_id'))


#with open("Stud.txt", "rt") as fin:
#    with open("out.txt", "wt") as fout:
#        for line in fin:
#            fout.write(line.replace('A', 'Orange'))

