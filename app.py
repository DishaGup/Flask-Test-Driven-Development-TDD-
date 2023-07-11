from flask import Flask, jsonify,request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>')
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return jsonify({'error': 'City not found'}), 404



@app.route("/weather",methods=["POST"])
def create_weather():
    data= request.get_json()
    city = data.get("city")
    if city in weather_data:
        return jsonify({"error":"City already Present"})
    else:
        weather_data[city] = {'temperature': data['temperature'], 'weather': data['weather']}
        return jsonify({'message': 'Weather data created successfully'}), 201

@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    if city in weather_data:
        data = request.get_json()
        if 'temperature' in data:
            weather_data[city]['temperature'] = data['temperature']
        if 'weather' in data:
            weather_data[city]['weather'] = data['weather']
        return jsonify({'message': 'Weather data updated successfully'}), 200
    else:
        return jsonify({'error': 'City not found'}), 404



@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': 'Weather data deleted successfully'}), 204
    else:
        return jsonify({'error': 'City not found'}), 404



if __name__ == '__main__':
    app.run()
