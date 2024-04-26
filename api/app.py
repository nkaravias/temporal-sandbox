from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Dictionary to store the landing zone data
landing_zones = {}

@app.route('/landing-zone', methods=['POST'])
def create_landing_zone():
    data = request.form
    appcode = data.get('appcode')
    tier = data.get('tier')
    label = data.get('label')
    if not appcode or not tier or not label:
        return jsonify({'error': 'Missing appcode, tier, or label'}), 400

    # Generate a unique ID for the landing zone
    lz_id = str(uuid.uuid4())
    # Generate a name using the label
    name = f"{label}-{tier}-{appcode}"
    landing_zones[lz_id] = {
        'appcode': appcode,
        'tier': tier,
        'name': name  # Store the generated name
    }
    return jsonify({'landing_zone_id': lz_id, 'name': name}), 201

@app.route('/landing-zone/<lz_id>', methods=['GET'])
def get_landing_zone(lz_id):
    if lz_id in landing_zones:
        return jsonify(landing_zones[lz_id])
    else:
        return jsonify({'error': 'Landing zone not found'}), 404

@app.route('/landing-zone', methods=['GET'])
def get_all_landing_zones():
    # Return a list of tuples with IDs and names
    return jsonify({lz_id: landing_zones[lz_id]['name'] for lz_id in landing_zones.keys()})

if __name__ == '__main__':
    app.run(debug=True)
