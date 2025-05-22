from flask import Flask, jsonify
from flask_cors import CORS
from kubernetes import client, config

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

def get_k8s_nodes():
    try:
        # Try in-cluster config first, fall back to kubeconfig
        try:
            config.load_incluster_config()
        except:
            config.load_kube_config()
        
        v1 = client.CoreV1Api()
        nodes = v1.list_node()
        
        node_info = []
        for node in nodes.items:
            # Get node name
            node_name = node.metadata.name
            
            # Get node internal IP
            internal_ip = None
            # for address in node.status.addresses:
            #     if address.type == 'InternalIP':
            #         internal_ip = address.address
            #         break
            
            internal_ip = node.metadata.annotations['alpha.kubernetes.io/provided-node-ip']

            # Determine node role
            role = "worker"
            labels = node.metadata.labels or {}
            status = True
            if node.spec.taints:
                for taint in node.spec.taints:
                    if taint.key == 'node.kubernetes.io/unreachable':
                        status = False
                        break
            
            # Check for control-plane/master node labels
            if 'node-role.kubernetes.io/control-plane' in labels:
                role = "control-plane"
            elif 'node-role.kubernetes.io/master' in labels:
                role = "master"
            
            node_info.append({
                'name': node_name,
                'internal_ip': internal_ip,
                'role': role,
                'labels': labels,  # Optional: include all labels
                'status': status
            })
        
        return node_info
    
    except Exception as e:
        return {'error': str(e)}

@app.route('/nodes', methods=['GET'])
def get_nodes():
    node_info = get_k8s_nodes()
    if isinstance(node_info, dict) and 'error' in node_info:
        return jsonify({
            'status': 'error',
            'message': node_info['error'],
            'nodes': []
        }), 500
        
    return jsonify({
        'status': 'success',
        'nodes': node_info
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)