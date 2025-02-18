import pyfiglet
font = pyfiglet.Figlet()
text = "Mr. Tech"
ascii_art = font.renderText(text)
print(ascii_art)

print ("Hellow there!")
print("welcome to Mr. Tech server Tool")
print("enter password please to continue.")
print("password: mrtech17")
password = "mrtech17"
while password != input("password:"):
    print("incorrect")
   
print("correct")

import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT),Handler) as httpd:
 print("starting serving at",PORT)
 print("Running: http://127.0.0.1:8080")
 print("cntlr C to exit")
 httpd.serve_forever()
 

 

   