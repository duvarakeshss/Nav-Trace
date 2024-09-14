import googlemaps
import heapq
import math

class ShortestPath:
    
    def __init__(self, api_key, start, end):
        self.api_key = api_key
        self.source = start  # Start should be a tuple of (latitude, longitude)
        self.destination = end  # End should be a tuple of (latitude, longitude)
        self.gmaps = googlemaps.Client(key=self.api_key)
        
    # Haversine distance for calculating the shortest distance between two points on a sphere
    def haversine_distance(self, lat1, lon1, lat2, lon2):
        # Radius of the Earth in kilometers
        R = 6371.0  
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c
    
    # A* algorithm for finding the shortest path
    def a_star(self, graph, start, goal):
        # Priority queue (min-heap) to store (cost, node) tuples
        queue = [(0, start)]  # Start should be in the form of (lat, lon)
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
                    # 'neighbor' and 'goal' are (lat, lon) tuples for Haversine
                    f_cost = tentative_g_cost + self.haversine_distance(*neighbor, *goal)  # Heuristic
                    heapq.heappush(queue, (f_cost, neighbor))
                    came_from[neighbor] = current
        
        return None  # No path found

    # Method to fetch directions and build a graph from Google Maps API
    def get_directions_and_find_shortest_path(self):
        # Get directions from Google Maps API
        directions_result = self.gmaps.directions(self.source, self.destination, alternatives=True)

        # Build a graph from the API response
        graph = {}
        waypoints = []
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
                    
                    # Store waypoints for the Google Maps link
                    waypoints.append((step['end_location']['lat'], step['end_location']['lng']))

        # Define start and goal locations for A*
        if directions_result:
            start_node = (directions_result[0]['legs'][0]['start_location']['lat'],
                          directions_result[0]['legs'][0]['start_location']['lng'])
            goal_node = (directions_result[0]['legs'][-1]['end_location']['lat'],
                         directions_result[0]['legs'][-1]['end_location']['lng'])

            # Run A* to find the shortest path
            shortest_path = self.a_star(graph, start_node, goal_node)

            # Display the shortest path
            if shortest_path:
                print("Shortest Path:")
                for node in shortest_path:
                    print(node)
            else:
                print("No path found.")

            # Generate a Google Maps link
            map_url = self.generate_google_maps_link()

            # Return the Google Maps link
            return map_url

        else:
            print("No directions found.")
            return None

    # Method to generate Google Maps link
    def generate_google_maps_link(self):
        directions_result = self.gmaps.directions(self.source, self.destination, alternatives=True)

        # Extract start and destination coordinates
        origin = directions_result[0]['legs'][0]['start_location']
        destination = directions_result[0]['legs'][-1]['end_location']
        
        # Extract waypoints
        waypoints = [f"{step['end_location']['lat']},{step['end_location']['lng']}" 
                     for leg in directions_result[0]['legs'] 
                     for step in leg['steps']]

        # Construct the Google Maps URL
        base_url = "https://www.google.com/maps/dir/"
        waypoints_str = '|'.join(waypoints)
        map_url = f"{base_url}{origin['lat']},{origin['lng']}/{destination['lat']},{destination['lng']}/data=!4m2!4m1!3e0"

        if waypoints:
            map_url += f"&waypoints={waypoints_str}"

        return map_url
