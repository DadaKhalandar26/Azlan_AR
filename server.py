from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve the 3D model file
@app.route('/models/simba.glb')
def serve_model():
    return send_from_directory(r"C:/Users/DELL/OneDrive/Desktop/Azlan_first_B-Day/Azlan_AR/models", "simba.glb")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Allows access from other devices
