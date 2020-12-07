#!/bin/bash
sudo apt update
sudo apt install ansible -y
sudo mkfs -t xfs /dev/sdd
sudo mkdir /data
sudo mount /dev/sdd /data
sudo -u ubuntu bash -c "cd /home/ubuntu; git clone https://github.com/Joseph-igbi/MAT-challenge.git" 
cd /home/ubuntu/MAT-challenge/ansible 
ansible-playbook playbook.yaml
newgrp docker
cd /home/ubuntu/MAT-challenge && docker-compose up -d
     

