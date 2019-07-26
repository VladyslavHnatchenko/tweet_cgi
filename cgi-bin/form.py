#!/usr/bin/env python
import cgi
import html


form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "not set")
text2 = form.getfirst("TEXT_2", "not set")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Processing form data</title>
        </head>
        </body>""")

print("<h1>Processing form data</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")
