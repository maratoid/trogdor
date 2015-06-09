# trogdor

## local cluster:
Fire up a local kraken cluster (you'll need to clone kraken repo)

Create benchmark controllers and services:

    kubectl create --cluster=local -f framework-controller.json
    kubectl create --cluster=local -f framework-service.json
    kubectl create --cluster=local -f load-controller-master.json
    kubectl create --cluster=local -f load-service-master.json
    kubectl create --cluster=local -f load-controller-slave.json
    kubectl create --cluster=local -f load-service-slave.json
    
Now you can go the http://172.16.1.103:8089/ and run a test.


Resize the number of frameworks:

    kub resize --cluster=local --replicas=20 rc framework

Run the http://172.16.1.103:8089/ test again. Compare results.

## aws cluster:
Fire up an aws kraken cluster (you'll need to clone kraken repo)

Create benchmark controllers and services

    kubectl create --cluster=local -f framework-controller.json
    kubectl create --cluster=local -f framework-service.json
    kubectl create --cluster=local -f load-controller-master.json
    kubectl create --cluster=local -f load-service-master.json
    kubectl create --cluster=local -f load-controller-slave.json
    kubectl create --cluster=local -f load-service-slave.json

### Create an elastic Load Balancer in EC2. 

On the AWS EC2 console:

1. Click "Load Balancers" under "Network & Security"
2. Click "Create Load Balancer"
3. Use the same naming schema as you did for creating other AWS resource. E.g. "trogdor-<your nick>"
4. Select "kubernetes-main" VPC
5. Do not check "Create an internal load balancer"
6. Use HTTP protocols, 80 as Load balancer port, 8089 as instance port
7. Select YOUR subnet (e.g. subnet-kubernetes-<your nick>)
8. Click "Assign Security groups", and select YOUR security group. E.g. secgroup-kubernetes-<your nick>. Make sure your security group is open on port 8089.
9. Select "configure security settings" and then "Configure healthcheck". 
10. Ping protocol is "TCP", Ping port is 30061. 
11. Select "Add EC2 instances". Add all YOUR nodes - node-01 thorugh node-x.
12. "Add tags" -> "Review and create"

After all nodes pass healthcheck, Locust load generator UI will be usable through the new ELB's public DNS name.

Now you can go the http://<ELB public DNS> and run a test.

Resize the number of frameworks while the test is running. Observe:

    kub resize --cluster=aws --replicas=20 rc framework