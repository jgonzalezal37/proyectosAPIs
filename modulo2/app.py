from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
]
 
def encuentraproximoid():
    return max(country["id"] for country in countries) + 1
 
@app.get("/countries")
def get_countries():
    return jsonify(countries)
 
@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = encuentraproximoid()
        countries.append(country)
        return country, 201
    return {"error": "Mandame un JSON"}, 415
 
def find_country_by_id(country_id):
    for country in countries:
        if country["id"] == country_id:
            return country
    return None
 
@app.patch("/countries/<int:country_id>")
def update_country(country_id):
    country = find_country_by_id(country_id)
    if country is None:
        return {"error": "Country not found"}, 404
 
    if request.is_json:
        data = request.get_json()
        for key, value in data.items():
            if key in country:
                country[key] = value
        return country
    else:
        return {"error": "Request must be JSON"}, 415