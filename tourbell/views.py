#tourbell/views.py

from django.shortcuts import render
import urllib.request


def get_Data(request):
    
    url = 'http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=1114052000'
    data_url = urllib.request.urlopen(url).readlines()
    
    wf = open( 'templates/main_page.html', 'w+')

    wf.write('''
    {% extends "base.html" %}
    
    {% block title %}Tourbell{% endblock %}
    
    {% load staticfiles %}
    {% block content %}
    <div id="content">
       <ul>
''')

    for name in data_url:
        name = name.decode().split('\n')
        if name[0][4:9] == 'wfKor':
            wf.write('%11s%s<h2>\n'%('<h2>',name[0][10:-8]))
    
    wf.write('''
       </ul>
    </div>
    {% endblock content %}
    ''')

    wf.close()

    return render(request, 'main_page.html')
