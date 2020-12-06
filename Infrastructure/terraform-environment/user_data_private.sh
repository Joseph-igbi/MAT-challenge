#!/bin/bash
                           
sudo apt update
sudo apt install git
sudo apt install ansible
git clone https://github.com/Joseph-igbi/MAT-challenge.git
cd ~/MAT-challenge/ansible && ansible-playbook playbook.yaml
newgrp docker
     

