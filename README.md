# trogdor

Fire up a local kraken cluster (you'll need to clone kraken repo)

Create benchmark controllers and services:

    kubectl create --cluster=local -f framework-controller.json
    kubectl create --cluster=local -f framework-service.json
    kubectl create --cluster=local -f load-controller.json
    kubectl create --cluster=local -f load-service.json
    
Now you can go the http://172.16.1.103:9081/ and run a 30-second test.


Resize the number of frameworks:

    kub resize --cluster=local --replicas=20 rc framework

Run the http://172.16.1.103:9081/ test again. Compare results.