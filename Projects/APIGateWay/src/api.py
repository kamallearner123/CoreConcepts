'''
API gateway:
    - API gateway is a server that acts as an API front-end, receiving API requests, enforcing throttling and security policies, passing requests to the back-end service, and then passing the response back to the requester.
    - API gateway provides a shared layer of security, caching, and management services, so that developers can focus on the business logic specific to their applications.
    - API gateway is a reverse proxy that exposes microservices as APIs.
    - API gateway handles all the incoming requests and routes them to the appropriate microservice.
    - API gateway can provide each client with a custom API.

API gateway features:
    - Authentication
    - Rate limiting
    - Load balancing
    - Caching
    - Request and response modifications
    - Logging and monitoring

API gateway benefits:
    - Security: API gateway can be used to authenticate and authorize incoming requests.
    - Rate limiting: API gateway can be used to limit the number of requests a client can make.
    - Load balancing: API gateway can be used to distribute incoming requests to multiple instances of a microservice.
    - Caching: API gateway can be used to cache the response of a microservice.
    - Request and response modifications: API gateway can be used to modify the request and response objects.
    - Logging and monitoring: API gateway can be used to log and monitor incoming requests.

API gateway use cases:
    - Microservices: API gateway can be used to expose microservices as APIs.
    - Mobile applications: API gateway can be used to provide a custom API for mobile applications.
    - Web applications: API gateway can be used to provide a custom API for web applications.
    - Third-party integrations: API gateway can be used to provide a custom API for third-party integrations.

API gateway implementation:
    - API gateway can be implemented using a reverse proxy server like Nginx or HAProxy.
    - API gateway can be implemented using a cloud-based service like AWS API Gateway or Google Cloud Endpoints.
    - API gateway can be implemented using a custom server like Express.js or Spring Cloud Gateway.

API gateway example:
    - An API gateway that exposes a microservice as an API.
    - An API gateway that authenticates incoming requests using JWT.
    - An API gateway that limits the number of requests a client can make.
    - An API gateway that distributes incoming requests to multiple instances of a microservice.
    - An API gateway that caches the response of a microservice.
    - An API gateway that logs and monitors incoming requests.

API gateway best practices:
    - Use HTTPS to secure the communication between the client and the API gateway.
    - Use JWT to authenticate incoming requests.
    - Use rate limiting to prevent abuse of the API.
    - Use load balancing to distribute incoming requests to multiple instances of a microservice.
    - Use caching to improve the performance of the API.
    - Use request and response modifications to customize the API for each client.
    - Use logging and monitoring to track the usage of the API.

API gateway challenges:
    - Scalability: API gateway needs to be able to handle a large number of incoming requests.
    - Security: API gateway needs to be able to authenticate and authorize incoming requests.
    - Performance: API gateway needs to be able to process incoming requests quickly.
    - Reliability: API gateway needs to be able to handle failures gracefully.
    - Monitoring: API gateway needs to be able to log and monitor incoming requests.

API gateway alternatives:
    - Direct communication: Instead of using an API gateway, clients can communicate directly with microservices.
    - Service mesh: Instead of using an API gateway, clients can use a service mesh to communicate with microservices.
    - Custom solution: Instead of using an API gateway, clients can build a custom solution to expose microservices as APIs.
    - Cloud-based solution: Instead of using an API gateway, clients can use a cloud-based solution to expose microservices as APIs.

API gateway future:
    - API gateway is expected to become more intelligent and automated.
    - API gateway is expected to provide more advanced security features.
    - API gateway is expected to provide more advanced monitoring and logging features.
    - API gateway is expected to become more integrated with other services.
    - API gateway is expected to become more customizable and extensible.

API gateway conclusion:
    - API gateway is a server that acts as an API front-end, receiving API requests, enforcing throttling and security policies, passing requests to the back-end service, and then passing the response back to the requester.
    - API gateway provides a shared layer of security, caching, and management services, so that developers can focus on the business logic specific to their applications.
    - API gateway is a reverse proxy that exposes microservices as APIs.
    - API gateway handles all the incoming requests and routes them to the appropriate microservice.
    - API gateway can provide each client with a custom API.

API gateway references:
    - https://www.nginx.com/api-gateway/
    - https://cloud.google.com/api-gateway
    - https://docs.aws.amazon.com/apigateway
    - https://www.nginx.com/resources/glossary/api-gateway/
    - https://www.nginx.com/blog/what-is-an-api-gateway/
    - https://www.nginx.com/blog/why-you-need-api-gateway/
    - https://www.nginx.com/blog/api-gateway-architecture/
    - https://www.nginx.com/blog/api-gateway-vs-service-mesh/
    - https://www.nginx.com/blog/api-gateway-vs-load-balancer/
    - https://www.nginx.com/blog/api-gateway-vs-reverse-proxy/
    - https://www.nginx.com/blog/api-gateway-vs-api-management/
    - https://www.nginx.com/blog/api-gateway-vs-api-proxy/
    - https://www.nginx.com/blog/api-gateway-vs-api-server/
    - https://www.nginx.com/blog/api-gateway-vs-api-gateway/
    - https://www.nginx.com/blog/api-gateway-vs-api-portal
    - https://www.nginx.com/blog/api-gateway-vs-api-gateway/
    - https://www.nginx.com/blog/api-gateway-vs-api-gateway/

API gateway summary:
    - API gateway is a server that acts as an API front-end, receiving API requests, enforcing throttling and security policies, passing requests to the back-end service, and then passing the response back to the requester.
    - API gateway provides a shared layer of security, caching, and management services, so that developers can focus on the business logic specific to their applications.
    - API gateway is a reverse proxy that exposes microservices as APIs.
    - API gateway handles all the incoming requests and routes them to the appropriate microservice.
    - API gateway can provide each client with a custom API.
'''

# Design an API gateway that exposes a microservice as an API.
# Implement an API gateway that authenticates incoming requests using JWT.
# Develop an API gateway that limits the number of requests a client can make.
# Create an API gateway that distributes incoming requests to multiple instances of a microservice.
# Build an API gateway that caches the response of a microservice.

# API gateway implementation using Flask
from flask import Flask, request, jsonify
import jwt
import datetime
import logging  # Logging module
import os


#####
ASSIGNMENTS_PATH = path = os.path.join(os.path.dirname(__file__), '../assignments')
IMAGES_PATH = path = os.path.join(os.path.dirname(__file__), '../images')
PAGES_PATH = path = os.path.join(os.path.dirname(__file__), 'pages/')

### Start program ###
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("./logs/"+__name__+".log") # Create a logger object with the name of the current module

from flask import Flask

app = Flask(__name__) # "__main__"
# CORS
from flask_cors import CORS
CORS(app)



@app.route('/')
def hello():
    with open(PAGES_PATH+'welcome.html', 'r') as f:
        print("###", os.getcwd()*10)
        return f.read()
    return "Hello, World!"

Assignments = '''
Fibnocci\n
Factoria\n
DFS\n
BFS'''
Assignments = Assignments.replace('\n', '<br>')

Response2 = f'''
<!-- templates/home.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RP Flask REST API</title>
</head>
<body>
    <h1>
        List of assignments: <br>
    </h1>
    <h2>
        {Assignments}
    </h2>
</body>
</html>
'''



logger.info("API Gateway started")

# Secret key for JWT
app.config['SECRET_KEY'] = "mysecretkey" # Secret key for JWT authentication 

# Mock microservice data
microservices = {
    "service1": "http://localhost:5001",
    "service2": "http://localhost:5002"
}

# Mock cache data
cache = {}

# Limit the number of requests a client can make
def limit_requests(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        user = payload['user']
        if user in cache:
            cache[user] += 1
        else:
            cache[user] = 1
        if cache[user] > 5:
            return False
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    
# Distribute incoming requests to multiple instances of a microservice
def distribute_request(service, data):
    if service in microservices:
        url = microservices[service]
        # Make a request to the microservice
        return requests.post(url, json=data)
    return None

# Cache the response of a microservice
def cache_response(service, data):
    cache[service] = data

# API endpoint to process requests
@app.route('/process', methods=['POST'])
def process_request():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Unauthorized"}), 401
        if not limit_requests(token):
            return jsonify({"message": "Too many requests"}), 429
        data = request.get_json()
        service = data.get('service')
        if not service:
            return jsonify({"message": "Service not specified"}), 400
        response = distribute_request(service, data)
        if not response:
            return jsonify({"message": "Service not found"}), 404
        cache_response(service, response.json())
        return jsonify(response.json())
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500


@app.route('/assignments/')
def assignments():
    # List of all the files from  the assignments folder and make json response to the client
    # Make html formatted response

    # Read all the files from the assignments folder
    
    files = os.listdir(ASSIGNMENTS_PATH)
    files = [f for f in files if f.endswith('.py')]
    files = [f.replace('.py', '') for f in files]

    # Make html formatted response
    Assignments = ''
    for f in files:
        Assignments += f + '<br>'
    # Mock descriptions for assignments
    descriptions = {
        "Fibnocci": "Calculate Fibonacci sequence",
        "Factoria": "Calculate factorial of a number",
        "DFS": "Depth First Search algorithm",
        "BFS": "Breadth First Search algorithm"
    }

    # Create table rows for assignments
    table_rows = ""
    for f in files:
        description = descriptions.get(f, "No description available")
        table_rows += f"<tr><td>{f}</td><td>{description}</td></tr>"

    Response = f'''
    <!-- templates/home.html -->

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>RP Flask REST API</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                text-align: center;
            }}
            h1 {{
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 10px;
                border: 1px solid #ddd;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>
                List of assignments:
            </h1>
            <table>
                <tr>
                    <th>Assignment</th>
                    <th>Description</th>
                </tr>
                {table_rows}
            </table>
        </div>
    </body>
    </html>
    '''
    return Response


# Function to create sqllite database to keep assignments and their descriptions
# Feilds should be id, assignment_name, description, Data strcture, Algorithm, Difficulty, Time complexity, Space complexity, Solution
# Read al the files from the assignments folder and get the description of the assignments
# Insert the data into the database
# Create an API endpoint to get the assignment details
# Create an API endpoint to get the assignment solution
# Create an API endpoint to submit the assignment solution
# Create an API endpoint to get the assignment status
# Create an API endpoint to get the assignment result
# Create an API endpoint to get the assignment feedback
# Create an API endpoint to get the assignment score
# Create an API endpoint to get the assignment leaderboard
# Create an API endpoint to get the assignment statistics
# Create an API endpoint to get the assignment summary
# Create an API endpoint to get the assignment report
# Create an API endpoint to get the assignment certificate
# Create an API endpoint to get the assignment badge
# Create an API endpoint to get the assignment completion
# Create an API endpoint to get the assignment verification
# Create an API endpoint to get the assignment validation
# Create an API endpoint to get the assignment evaluation
# Create an API endpoint to get the assignment assessment
# Create an API endpoint to get the assignment analysis
# Create an API endpoint to get the assignment analytics
# Create an API endpoint to get the assignment audit
# Create an API endpoint to get the assignment review
# Create an API endpoint to get the assignment rating
# Create an API endpoint to get the assignment feedback
# Create an API endpoint to get the assignment comments
# Create an API endpoint to get the assignment suggestions
# Create an API endpoint to get the assignment improvements
# Create an API endpoint to get the assignment enhancements
# Create an API endpoint to get the assignment updates
# Create an API endpoint to get the assignment changes
# Create an API endpoint to get the assignment modifications
# Create an API endpoint to get the assignment revisions
# Create an API endpoint to get the assignment versions

def create_database():
    # Create a sqllite database
    # Create a table with the following fields
    # id, assignment_name, description, Data strcture, Algorithm, Difficulty, Time complexity, Space complexity, Solution

    db = sqlite3.connect('assignments.db')
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE assignments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        assignment_name TEXT,
        description TEXT,
        data_structure TEXT,
        algorithm TEXT,
        difficulty TEXT,
        time_complexity TEXT,
        space_complexity TEXT,
        solution TEXT
    )
    ''')

    db.commit()


def insert_data():
    # Read all the files from the assignments folder
    # Get the description of the assignments
    # Insert the data into the database

    db = sqlite3.connect('assignments.db')
    cursor = db.cursor()

    files = os.listdir(ASSIGNMENTS_PATH)
    files = [f for f in files if f.endswith('.py')]
    files = [f.replace('.py', '') for f in files]

    # Mock descriptions for assignments
    descriptions = {
        "Fibnocci": "Calculate Fibonacci sequence",
        "Factoria": "Calculate factorial of a number",
        "DFS": "Depth First Search algorithm",
        "BFS": "Breadth First Search algorithm"
    }

    for f in files:
        description = descriptions.get(f, "No description available")
        cursor.execute('''
        INSERT INTO assignments(assignment_name, description)
        VALUES(?, ?)
        ''', (f, description))

    db.commit()



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True) # 127.0.0.1, 192.168.10.110

### End program ###
    names = {
    "Adithya": "Apple",
    "Rahul": "Meta",
    "Sai": "Google",
    "Srinivas": "Amazon",
    "Sandeep": "Microsoft",
    "david": "Facebook",
    "james": "Amazon",
    "michael": "Amazon",
    "john": "Instagram",
    "robert": "Amazon",
    "william": "Snapchat",
    "joseph": "Pinterest"}
