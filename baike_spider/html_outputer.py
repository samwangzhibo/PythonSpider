#coding:utf-8
'''
Created on 2016-3-30

@author: zybang
'''

    
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.fout = open('output.html', 'w')

    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        #self.fout = open('output.html', 'w')
        
        
        self.fout.write("<html>")
        self.fout.write("<body>")
        
        #以免乱码
        self.fout.write("<head>")
        self.fout.write('<meta charset="utf-8">')
        self.fout.write("</head>")
        
        
        self.fout.write("<table>")
        
        #ascii 
        for data in self.datas:
            self.fout.write("<tr>")
            self.fout.write("<td>%s</td>" % data['url'])
            self.fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            self.fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            self.fout.write("</tr>")
        
        self.fout.write("</table>")
        self.fout.write("</body>")
        self.fout.write("</html>")
        self.fout.close()
    
    
    
    
    
    



