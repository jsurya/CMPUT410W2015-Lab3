#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('name')
val2 = form.getvalue('family')
print """Content-type: text/html

Your name is: %s  <br/>
Your family is: %s <br/>
<br/>"""%(val1, val2)


print """ <form method = "post" action = "index.py">
	Enter your birthdate: <input type ="date" name = "birthdate"><br/>
	Enter your main hobby: <input type ="text" name = "main-hobby"><br/>
<input type = "submit" value = "Submit">
</form>"""

