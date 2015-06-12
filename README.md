# trogdor

## Running:
Fire up a kraken cluster (you'll need to clone kraken repo)

Create benchmark controllers and services:

    kubectl create --cluster='type of cluster' -f kub

## local cluster

Create local service:
 
    kubectl create --cluster=local -f kub-local

Now you can go the http://172.16.1.103:8089/ and run a test.

## aws cluster

### Create an elastic Load Balancer in EC2. 

On the AWS EC2 console:

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
11. Select "Add EC2 instances". Add all YOUR nodes - node-01 thorugh node-x.
12. "Add tags" -> "Review and create"

Update your aws settings.yaml file. Add

    elb: name_of_your_elb

to aws section of the config

Create aws service:
 
    kubectl create --cluster=aws -f kub-aws
    
After all nodes pass healthcheck, Locust load generator UI will be usable through the new ELB's public DNS name.

Now you can go the http://ELB-public-DNS and run a test.

## scaling (on aws)
Resize the number of load generator slaves while the test is running. Observe:

    kub scale --cluster=aws --replicas=300 rc load-generator-slave

You should see numbr of slaves at http://ELB-public-DNS go up shortly

Resize the number of frameworks while the test is running. Observe:

    kub resize --cluster=aws --replicas=50 rc framework