#!/bin/bash
sudo apt update
sudo apt install ansible -y
sudo -u ubuntu bash -c "cd /home/ubuntu; git clone --branch bastion https://github.com/Joseph-igbi/MAT-challenge.git" 
cd /home/ubuntu/MAT-challenge
ansible-playbook playbook.yaml


     

