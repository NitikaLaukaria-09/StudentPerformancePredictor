from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(length))

        score = (
            data['previous_score'] * 0.5
            + data['attendance'] * 0.3
            + data['study_hours'] * 2
        )

        result = min(100, round(score))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(
            json.dumps({"result": result}).encode()
        )

print("Server running at http://localhost:8000")
HTTPServer(("localhost", 8000), Handler).serve_forever()