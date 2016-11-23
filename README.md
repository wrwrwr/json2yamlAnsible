# json2yamlAnsible
Project for taking the output of JSON from AWS and converting it into useful Ansible Playbooks http://docs.ansible.com/ansible/ec2_group_module.html 


The Problem:

JSON, Just kidding. With some good bash skills you can get a lot of your infrastructure in the format of json files. One of the projects I am 
taking on is converting the GUI usage of the AWS console. Managing the Security Group creation, care all through Ansible Playbooks.

I have used Chef and Puppet in the past at a very low level. But Ansible seems to be SOOOO much easier.

You can imagine hand editing JSON into Yaml output is quite tiresome. So, I googled and found no script out there that is capable
of ingesting say 'sg-XXXXX' in json, and converting it to the format seen here:
http://docs.ansible.com/ansible/ec2_group_module.html
