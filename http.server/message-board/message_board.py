#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []

form = '''
<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>

'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        # use get so that no error when there's no content-length property in the headers
        length = int(self.headers.get("Content-length", 0))

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

        # parse the message
        message = parse_qs(data)["message"][0]
        # Escape HTML tags in the message so users can't break world+dog.
        message = message.replace("<", "&lt;")

        # Store it in memory.
        memory.append(message)

        # redirect back to root page (status code 303)
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()
    
    def do_GET(self):
        # send 200 OK response
        self.send_response(200)

        # send headers
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # response body: send the form with the messages in it
        mesg = form.format("\n".join(memory))
        self.wfile.write(form.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
