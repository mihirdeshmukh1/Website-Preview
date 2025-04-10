import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Set the working directory to the folder containing the generated HTML
os.chdir('generated')  # Make sure to navigate to the folder where the generated HTML is saved

# Define the port (8000 is commonly used)
PORT = 8000

# Create the server and bind it to the port
Handler = SimpleHTTPRequestHandler
httpd = TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
