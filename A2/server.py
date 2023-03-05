import sys;
from http.server import HTTPServer, BaseHTTPRequestHandler;
import MolDisplay

class MyHandler( BaseHTTPRequestHandler ):
    def do_GET(self):
        if self.path == "/":
            self.send_response( 200 ); # OK
            self.send_header( "Content-type", "text/html" );
            self.send_header( "Content-length", len(home_page) );
            self.end_headers();

            self.wfile.write( bytes( home_page, "utf-8" ) );

        else:
            self.send_response( 404 );
            self.end_headers();
            self.wfile.write( bytes( "404: not found", "utf-8" ) );

    def do_POST(self):
        if self.path == "/molecule":
          mol = MolDisplay.Molecule();

          for i in range (4):
            self.rfile.readline()
            
          mol.parse(self.rfile);
          mol.sort()
          temp = mol.svg()
          self.send_response( 200 ); #ok
          self.send_header( "Content-type", "image/svg+xml" );
          self.send_header( "Content-length", len(temp) );
          self.end_headers();
          self.wfile.write( bytes( temp, "utf-8" ) );


        else:
            self.send_response( 404 );
            self.end_headers();
            self.wfile.write( bytes( "404: not found", "utf-8" ) );



home_page = """
<html>
 <head>
 <title> File Upload </title>
 </head>
 <body>
 <h1> File Upload </h1>
 <form action="molecule" enctype="multipart/form-data" method="post">
 <p>
 <input type="file" id="sdf_file" name="filename"/>
 </p>
 <p>
 <input type="submit" value="Upload"/>
 </p>
 </form>
 </body>
</html>
""";

httpd = HTTPServer( ( 'localhost', int(sys.argv[1]) ), MyHandler );
httpd.serve_forever();
