from urllib.parse import urlencode

# List of coordinates
coordinates = [
(11.0256315, 77.00412039999999),
(11.0241817, 77.0051343),
(11.0129398, 76.9861492),
(11.0044381, 76.9930368),
(10.9972005, 76.9957349),
(10.997194, 76.9958525),
(10.9647118, 76.9876043),
(10.9498072, 77.0000328),
(10.9241232, 76.98286089999999),
(10.917951, 76.9860578),
(10.8342314, 77.0171112),
(10.746312, 77.020006),
(10.7448453, 77.0197603),
(10.7445227, 77.0201866),
(10.7416404, 77.0580423),
(10.7406532, 77.059314),
(10.7406533, 77.05940319999999),
(10.7399939, 77.0603423),
(10.7303415, 77.0688081),
(10.7257708, 77.06795269999999),
(10.7071304, 77.0713308),
(10.7022968, 77.0707381),
(10.7000676, 77.0703809),
(10.7001793, 77.06986189999999),
(10.6985697, 77.06896669999999),
(10.6918329, 77.0682104),
(10.6916451, 77.06859),
(10.6897099, 77.08369069999999),
(10.6878073, 77.0947443),
(10.6873489, 77.0939825),
]

# Define origin and destination
origin = coordinates[0]
destination = coordinates[-1]

# Format waypoints
waypoints = '|'.join([f"{lat},{lng}" for lat, lng in coordinates[1:-1]])

# Base URL for Google Maps Directions
base_url = "https://www.google.com/maps/dir/"

# Construct the URL
url = f"{base_url}{origin[0]},{origin[1]}/{destination[0]},{destination[1]}/@{origin[0]},{origin[1]},12z/data=!4m2!4m1!3e9?entry=ttu&g_ep=EgoyMDI0MDkxMS4wIKXMDSoASAFQAw%3D%3D"

# Add waypoints
if waypoints:
    url += f"&waypoints={waypoints}"

print(url)
