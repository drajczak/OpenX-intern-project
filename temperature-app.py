from flask import Flask, request, jsonify
import uuid

# Create flask app
app = Flask(__name__)

# Generate unique app identifier as a string to be easier to work with json
app_id = str(uuid.uuid4())

@app.route('/convert', methods=['GET'])
def convert_temp():
	# Get Fahrenheit temperature from query parameters
	fahrenheit = request.args.get('fahrenheit', type=float)
	# Handle incorrect or missing data
	if fahrenheit is None:
		return jsonify(({'error': 'No temperature provided'}), 400) # 400 is status code for "Bad Request"

	# Convert Fahrenheit to Celsius
	celsius = (fahrenheit - 32) * 5.0 / 9.0

	# Return the result and the app ID
	return jsonify({
		'celsius': round(celsius, 2),
		'app_id': app_id
	})

# Run the app
if __name__ == '__main__': # Check if script is running as the main program
	app.run(host='0.0.0.0', debug=True) # Start the Flask application in debug mode and make it accessible on all network interfaces by setting host to '0.0.0.0'. This allows external devices to connect to the app.

