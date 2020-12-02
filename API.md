# API documentaion
The API is interactively explorable at [http:localhost:8000/api/v1](http://localhost:8000/api/v1) when the Django server is running.

## measurements

### GET
List of idividual measurements.
```
http://localhost:8000/api/v1/measurements/
```
**Optional parameters**:
|parameter|type|Description|
|-----|-----|-----|
|location__city__name|string|Limit results by a certain city|
|parameter__name|string|Limit results by a certain parameter, e.g. `pm25`, `no2`, etc.|

**Success 200**:

Sample response:
```json
{
  "count": 100,
  "next": null,
  "previous": null,
  "results": [
    {
      "parameter": {
        "name": "pm10",
        "description": "Particulate matter less than 10 micrometers in diameter",
        "preferred_unit": "µg/m³"
      },
      "value": 30.0,
      "date": "2020-11-30T21:00:00Z"
    },
    {
      "parameter": {
        "name": "no2",
        "description": "Nitrogen Dioxide",
        "preferred_unit": "ppm"
      },
      "value": 1.007,
      "date": "2020-11-30T21:00:00Z"
    },
    ...
```

### POST
Add an idividual measurement.
```
http://localhost:8000/api/v1/measurements/add/
```

Sample request:
```bash
curl -d '{"parameter": "no2", "date": "2020-11-30T21:00:00Z", "value": 3.14, "city": "SWEETWATER"}' -H 'content-type: application/json' "http://localhost:8000/api/v1/measurements/add/"
```
and response:
```json
{
  "messge": "Measurement saved to database",
  "data": {
    "parameter": "no2",
    "date": "2020-11-30T21:00:00Z",
    "value": 3.14,
    "city": "SWEETWATER"
  }
}
```


## locations
List of locations of measurements:
```
http://localhost:8000/api/v1/locations/
```


## cities
List of US cities:
```
http://localhost:8000/api/v1/cities/
```
The above endpoint also accepts POST requests to add new cities, e.g.
```bash
http "http://localhost:8000/api/v1/cities/" name=Sacramento country=US
```
with response:
```json
{
    "country": "US",
    "id": 47,
    "name": "Sacramento"
}
```

Indivdual city detail by its database id (integer):
```
http://localhost:8000/api/v1/cities/:id
```

## parameters
List of parameters, a.k.a. units, used for measurements:
```
http://localhost:8000/api/v1/parameters/
```

The above endpoint also accepts POST requests to add new cities, e.g.
```bash
http "http://localhost:8000/api/v1/parameters/" name=o4 description="This is a description" preferred_unit='ppb'
```
with response:
```json
{
    "description": "This is a description",
    "name": "o4",
    "preferred_unit": "ppb"
}
```

Indivdual parameter detail by its database id (integer):
```
http://localhost:8000/api/v1/cities/:id
```
