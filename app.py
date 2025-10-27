from flask import Flask
import redis
import os

# Create Flask app
app = Flask(__name__)

# Connect to Redis using environment variables for flexibility
r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),  # default to localhost
    port=int(os.environ.get("REDIS_PORT", 6379))     # default port 6379
)

# Home page route
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Count page route
@app.route('/count')
def count():
    # Increment the visit counter in Redis
    r.incr('hits')
    
    # Get the current count and convert to string
    visits = r.get('hits').decode('utf-8')
    
    return f'This page has been visited {visits} times.\n'

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
