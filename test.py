import googlemaps
import heapq
import math

# Initialize the Google Maps client
api_key = 'AIzaSyAyHmK4lf7nriSYK_WzZvhNb0IJdUcohwg'
gmaps = googlemaps.Client(key=api_key)

# Helper function to calculate Euclidean distance (Haversine Formula) as the heuristic for A*
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# A* algorithm implementation
def a_star(graph, start, goal):
    # Priority queue (min-heap) to store (cost, node) tuples
    queue = [(0, start)]
    heapq.heapify(queue)
    
    # Dictionaries to store the cost of reaching each node and the path taken
    g_costs = {start: 0}
    came_from = {start: None}
    
    while queue:
        _, current = heapq.heappop(queue)
        
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse the path
        
        # Explore neighbors
        for neighbor, distance in graph[current].items():
            tentative_g_cost = g_costs[current] + distance
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + haversine_distance(*neighbor, *goal)  # Heuristic
                heapq.heappush(queue, (f_cost, neighbor))
                came_from[neighbor] = current
    
    return None  # No path found

# Define source and destination
source = "Psg college of technology,Peelamedu"
destination = "Gollapatti,pollachi"

# Request directions from Google Maps
directions_result = gmaps.directions(source, destination, alternatives=True)

# Build a graph from the API response
graph = {}
for route in directions_result:
    for leg in route['legs']:
        for step in leg['steps']:
            start_location = (step['start_location']['lat'], step['start_location']['lng'])
            end_location = (step['end_location']['lat'], step['end_location']['lng'])
            distance = step['distance']['value'] / 1000.0  # Distance in kilometers
            
            # Add bidirectional edges to the graph
            if start_location not in graph:
                graph[start_location] = {}
            if end_location not in graph:
                graph[end_location] = {}
            
            graph[start_location][end_location] = distance
            graph[end_location][start_location] = distance

# Define start and goal locations for A*
if directions_result:
    start_node = (directions_result[0]['legs'][0]['start_location']['lat'],
                  directions_result[0]['legs'][0]['start_location']['lng'])
    goal_node = (directions_result[0]['legs'][-1]['end_location']['lat'],
                 directions_result[0]['legs'][-1]['end_location']['lng'])

    # Run A* to find the shortest path
    shortest_path = a_star(graph, start_node, goal_node)

    # Display the shortest path
    if shortest_path:
        print("Shortest Path:")
        for node in shortest_path:
            print(node)
    else:
        print("No path found.")
else:
    print("No directions found.")
