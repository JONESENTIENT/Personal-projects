import os
import webbrowser
name = input('Enter the website name : ')
color1 = input('Enter primary color :')
color2 = input('Enter secondary color :')
content = input('Enter the content to display :')

site_code = '''<!DOCTYPE html>
<html>
<head>
</head>
<body bgcolor=''' + color1 + '''>
   <h1>name}</h1>
{content}
</body>
</html>'''

html_file_path = 'temp_html_file.html'
with open(html_file_path, 'w') as html_file:
    html_file.write(site_code)

webbrowser.open(f'file://{os.path.abspath(html_file_path)}')