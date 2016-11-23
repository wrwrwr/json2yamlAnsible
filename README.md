# json2yamlAnsible
Project for taking the output of JSON from AWS and converting it into useful Ansible Playbooks http://docs.ansible.com/ansible/ec2_group_module.html 


The Problem:

JSON, Just kidding. With some good bash skills you can get a lot of your infrastructure in the format of json files. One of the projects I am 
taking on is converting the GUI usage of the AWS console. Managing the Security Group creation, care all through Ansible Playbooks.

I have used Chef and Puppet in the past at a very low level. But Ansible seems to be SOOOO much easier.

You can imagine hand editing JSON into Yaml output is quite tiresome. So, I googled and found no script out there that is capable
of ingesting say 'sg-XXXXX' in json via sysargs, and converting it to the format seen here:
http://docs.ansible.com/ansible/ec2_group_module.html


Running this script is very easy

./json2yaml.py sg-XXXXXX  <--- json file attained from a routine call of 

"aws ec2 describe-security-groups --group-ids sg-XXXXXX > sg-XXXXXX" #Where sg-XXXXXX is a SG-id of your choice. 

This script could be leveraged with a simple for i loop to pull down all json files of your SG's then run another bash loop to convert it into Ansible (yaml) format.

ansible-playbook -i /etc/ansible/local SG-XXXXXX.yml.out and your done!

See this AWESOME video about how to leverage Ansible for AWS. It was an eye opener for me.

https://youtu.be/fxVqo7nomfA?list=PLaDgRSbFYikeJ4SwaE2QnjudjMZuJvq0g
