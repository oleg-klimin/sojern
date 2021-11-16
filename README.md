
How to run it:
1. Clone this repository 
`git clone https://github.com/oleg-klimin/sojern.git`
2. To run Util - 'compare versions':
- Switch to **compare_versions** folder 
`cd sojern/compare_versions`
- Give files executable permissions
` chmod +x compare_versions*`
- run `compare_versions.py` or `compare_versions.py` with versions numbers as an arguments
Example:`compare_versions.py 1.2.9.9.9.9 1.3.4` 

3. To apply Kubernetes deployment manifest:
 - Switch to **kubernetes_deployment** folder
 `cd sojern/kubernetes_deployment`
 - run `kubectl apply -f k8s.yaml`
 
 Expected that:
- you have Kubernetes cluster and **kubectl** is set up to work with it


