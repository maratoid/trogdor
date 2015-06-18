# trogdor

## Running:

## local cluster
Adjust number of nodes in your local settings.yaml

Fire up local kraken cluster (you'll need to clone kraken repo)

   kraken local up

Create benchmark controllers and services:

    kubectl create --cluster=local -f kub

Create local service:
 
    kubectl create --cluster=local -f kub-local

Now you can go the http://172.16.1.103:8089/ and run a test.

## aws cluster

Adjust number of nodes in your aws settings.yaml

Create an elastic Load Balancer in EC2. On the AWS EC2 console:

1. Click "Load Balancers" under "Network & Security"
2. Click "Create Load Balancer"
3. Use the same naming schema as you did for creating other AWS resource. E.g. "trogdor-your-nick"
4. Select "kubernetes-main" VPC
5. Do not check "Create an internal load balancer"
6. Use HTTP protocols, 80 as Load balancer port, 8089 as instance port
7. Select YOUR subnet (e.g. subnet-kubernetes-your-nick)
8. Click "Assign Security groups", and select YOUR security group. E.g. secgroup-kubernetes-your-nick. Make sure your security group is open on port 8089.
9. Select "configure security settings" and then "Configure healthcheck". 
10. Ping protocol is "TCP", Ping port is 30061. 
11. No instances to add yet. They will be automatically added by Vagrant later.
12. "Add tags" -> "Review and create"

Update your aws settings.yaml file. Add

    elb:                                                       
       name: name_of_your_elb
       dns_name: your_nickname.kubeme.io                                                   
       balancer_port: 80                                       
       instance_port: 30061                                      
       healthy_threshold: 2                                     
       unhealthy_threshold: 3                                   
       timeout: 5                                               
       interval: 30                                             
       target_port: 30061    

to aws section of the config

Fire up aws kraken cluster (you'll need to clone kraken repo)

    kraken aws up

Create benchmark controllers and services:

    kubectl create --cluster=aws -f kub

Create aws service:
 
    kubectl create --cluster=aws -f kub-aws
    
After all pods become ready, Locust load generator UI will be usable. Now you can go the http://your_nickname.kubeme.io and run a test.

## scaling (on aws)
Resize the number of load generator slaves while the test is running. Observe:

    kub scale --cluster=aws --replicas=300 rc load-generator-slave

You should see numbr of slaves at http://your_nickname.kubeme.io go up shortly

Resize the number of frameworks while the test is running. Observe:

    kub resize --cluster=aws --replicas=50 rc framework
