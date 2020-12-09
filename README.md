# MAT-challenge

## Prerequisites:
* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
* AWS Account

## Introduction
The challenge was to develop an application which subscribes to the provided MQTT broker and consumes data from the given MQTT topic, stores it to a meaningful medium while also providing a visualisation tool to read the collected data.

The app developed runs in a python based docker container and an InfluxDB container was created for data storage. Both run on the same network as the MQTT broker to allow communication. Grafana is configured on the Instance using ansible, for data visualisation. 

## Deployment

The application can be deployed in your environment by:
* In MAT-challenge/ansible running "$ ansible-playbook playbook.yaml" to configure the VM with the app dependencies which includes:
  * *Terraform*
  * *docker* 
  * *docker-compose*
  * *grafana*
  * *python3 and pip3*
  * *eksctl*
  * *kubectl*
  * *aws cli*
* After the configuration is complete, in MAT-challenge/ run "$ docker-compose up -d"
* The app will be up and running and grafana which has been installed by Ansible can be viewed on localhost:3000

## Automated environment and deployment
Alternatively, the below Bastion host environment can be created and the deployment automated by: 
##### Note that an EC2 user or IAM role with full EC2 and VPC permissions is needed to deploy the environment. Different authentication methods for terraform are shown [here](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* In MAT-challenge/Infrastructure/terraform-environment/variables.tf change the variable "key_name" to the name of a Key pair you have access to
* Using terraform, in MAT-challenge/Infrastructure/terraform-environment run "$ terraform apply"
* This builds the below environment in AWS. Through the user data, Ansible is automatically run to configure the environment in both instances and the app is automatically deployed in docker containers in the private subnet for added security.
* The IAC also deploys an EBS-Volume which is mounted on launch through the user data. The InfluxDB volume data is stored in the mounted EBS-volume to ensure persistence, should anything happen to the EC2 instance.
* The private instance can be accessed through ssh-agent forwarding though this should not be needed as the deployment is automatic.
![structure]

## Data visualisation
When run in your own environment, Grafana can be accessed on port 3000. If using the above infrastructure, Grafana has been installed on the public instance and can also be accessed on port 3000.
* The default user name and password for Grafana is admin. This will have to be changed on logging in
* Add an InfluxDB database source 
* If using the above infrastructure the database url is "http://<private_ip_of_private_instance>:8086" otherwise it is "http://localhost:8086"
* The Database name is "mclarenDB" and for this task the User and Password have been set to admin
* After adding the datasource, you can proceed to create the dashboard.

#### Dashboard
![grafana]

## Scaling
To easily scale, the app will have to be deployed to kubernetes. The dependencies for this are included in the ansible configuration.

* Firstly you'll have to authenticate with AWS using a user with eks permisions. Run "$ aws configure" and provide the user authentication details. 
* Run "eksctl create cluster --name=<cluster_name> --ssh-public-key=<KEY_NAME> --node-type=<node_type>" and wait for the cluster to be created.
* To deploy the app, in MAT-challenge/kubernetes run "$ kubectl apply -f .". Grafana can be viewed on port 3000
* To autoscale with a max of 3 replicas run"$ kubectl autoscale deployment processapp --max 3 --min 1 --cpu-percent 75"




[structure]: https://i.imgur.com/sYsW0Oj.png
[grafana]: https://i.imgur.com/U5N3c2h.png
