#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

print """ Content-type: text/html

<form method = "post" action = "form.py">
	Enter your name: <input type ="text" name = "name"><br/>
	Enter your family: <input type ="text" name = "family">
	<br/>
<input type = "submit" value = "Submit">
</form>"""

val1 = form.getvalue('birthdate')
val2 = form.getvalue('main-hobby')
if (val1 or val2) != None: 
	print "Your birth date is: %s <br/>"%(val1)
	print
	print "Your main-hobby is: %s <br/>"%(val2)


