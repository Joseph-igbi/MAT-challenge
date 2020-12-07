# MAT-challenge

## Prerequisites:
* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
* AWS Account

## Introduction
The challenge was to develop an application which subscribes to the provided MQTT broker and consumes data from the given MQTT topic, stores it to a meaninggul medium while also provicing a visualisation tool to read the collected data.

The app developed runs in a python based docker container and an InfluxDB container was created for data storage. Both run on the same network as the MQTT broker to allow communication. Grafana is configured on the Instance using ansible, for data visualisation. 

## Deployment

The application can be deployed in your environment by:
* In MAT-challenge/ansible running "$ ansible-playbook playbook.yaml" to configure VM with the app dependencies which includes
  * *Terraform*
  * *docker* 
  * *docker-compose*
  * *grafana*
  * *python3 and pip3*
* After the configuration is complete, in MAT-challenge/ run "$ docker-compose up -d"
* The app will be up and running and as grafana has been install by Ansible can be viewed on localhost:3000

## Automated environment and deployment
However the below Bastion host environment can be created and the deployment automated by: 
##### Note an EC2 user or IAM role with full EC2 and VPC permissions is needed to deploy the environment. Different authentication methods for terraform are shown [here](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* In MAT-challenge/Infrastructure/terraform-environment/variables.tf change the variable "key_name" to the name of a Key pair you have access to
* Using terraform, in MAT-challenge/Infrastructure/terraform-environment run "$ terraform apply"
* This builds the below environment in AWS. Through the user data, Ansible is automatically run to configure the environment in both instances and the app is automatically deployed in docker containers in the private subnet for added security.
* The IAC also deploys an EBS-Volume which is mounted on launch through the user data. The InfluxDB volume data is stored in the mounted EBS-volume to ensure persistence, should anything happen to the EC2 instance.
* The private instance can be accessed through ssh-agent forwarding though this should not be needed as the deployment is automatic
![structure]

## Data visualisation
When ran in your own environment, Grafana can be accessed on port 3000. If using the above infrastructure, Grafana has been installed on the public instance and can also be accessed on port 3000.
* The default user name and password for Grafana is admin. This will have to be changed on logging in
*
* 










[structure]: https://i.imgur.com/sYsW0Oj.png
