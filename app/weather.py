from flask import Flask, jsonify,request

def create_app():
    app = Flask(__name__)

    @app.route("/weather/<string:city>")
    def get_weather_by_city(city):
        weather = weather_data.get(city)
        if weather:
           return jsonify(weather), 200
        else:
          return jsonify({"error": "Weather data not found"}), 404
        
    @app.route("/weather", methods=["POST"])
    def add_weather_data():
        data = request.get_json()
        city = data.get("city")
        temperature = data.get("temperature")
        weather = data.get("weather")

        if city and temperature and weather:
           weather_data[city] = {"temperature": temperature, "weather": weather}
           return jsonify({"message": "Weather data added successfully"}), 200
        else:
           return jsonify({"error": "Invalid request data"}), 400
        
    @app.route("/weather/<string:city>", methods=["DELETE"])
    def delete_weather_data(city):
       if city in weather_data:
        del weather_data[city]
        return jsonify({"message": "Weather data deleted successfully"}), 200
       else:
        return jsonify({"error": "City not found"}), 404
       

     
    @app.route("/weather/<string:city>", methods=["PUT"])
    def update_weather_data(city):
      if city in weather_data:
        data = request.get_json()
        temperature = data.get("temperature")
        
        if temperature:
            weather_data[city]["temperature"] = temperature


            return jsonify({"message": "Weather data updated successfully"}), 200
        else:
            return jsonify({"error": "City not found in the Weather data."}), 404

        
    return app

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


if __name__ == "__main__":
    app = create_app()
    app.run()
