#!/bin/bash
                           
sudo apt update
sudo apt install git
sudo apt install ansible
git clone --branch bastion https://github.com/Joseph-igbi/MAT-challenge.git
cd ansible && ansible-playbook playbook.yaml
     

