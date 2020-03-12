from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from io import StringIO
import logging

list = [
    {'no': 10, 'name': 'name1', 'location': 'ShangHai'},
    {'no': 12, 'name': 'name2', 'location': 'BeiJin'},
    {'no': 14, 'name': 'name3', 'location': 'ChengDu'}
]


def index2(request):
    # output=StringIO()
    # output.write('<html>\n')
    # output.write('<head>\n')
    # output.write('\t<meta charset="utf-8">\n')
    # output.write('\t<title>index2 page</title>')
    # output.write('</head>\n')
    # output.write('<body>\n')
    # output.write('\t<h1>base_app2</h1>\n')
    # output.write('\t<hr>\n')
    # output.write('\t<table>\n')
    # output.write('\t\t<tr>\n')
    # output.write('\t\t\t<th width=120>base_app编号</th>\n')
    # output.write('\t\t\t<th width=180>base_app名称</th>\n')
    # output.write('\t\t\t<th width=180>base_app所在地</th>\n')
    # output.write('\t\t</tr>\n')
    # for l in list:
    #     output.write('\t\t<tr>\n')
    #     output.write(f'\t\t\t<td align=center>{l["no"]}</td>\n')
    #     output.write(f'\t\t\t<td align=center>{l["name"]}</td>\n')
    #     output.write(f'\t\t\t<td align=center>{l["location"]}</td>\n')
    #     output.write('\t\t</tr>\n')
    # output.write('\t</table>\n')
    # output.write('</body>\n')
    # output.write('</html>\n')
    # return HttpResponse(output.getvalue())
    # -----------------------------
    # return HttpResponse("<h1>Hello Django . </h1>")
    #logging.warning('Watch out!')  # 消息会被打印到控制台上
    #logging.info('I told you so')  # 这行不会被打印，因为级别低于默认级别

    #logging.basicConfig(filename='/base_app2/log/example.log', level=logging.DEBUG)
    #logging.debug('This message should go to the log file')
    #logging.info('So should this')
    #logging.warning('And this, too')


    return render(request, 'index2.html', {"li": list})
