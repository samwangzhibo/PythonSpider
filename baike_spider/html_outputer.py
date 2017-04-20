#coding:utf-8
'''
Created on 2016-3-30

@author: zybang
'''

    
class HtmlOutputer(object):
    def __init__(self):
        self.datas = [] #列表(数组)
        self.fout = open('output.html', 'w')
        self.init_header();

    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def init_header(self):
        self.fout.write("<html>")
        self.fout.write("<body>")
        
        #以免乱码
        self.fout.write("<head>")
        self.fout.write('<meta charset="utf-8">')
        self.fout.write("</head>")
        
        self.fout.write("<table>")
    
    def output_html(self, datas):
        #self.fout = open('output.html', 'w')
        
        #ascii 
        for data in datas:
            try:
                self.fout.write("<tr>")
                self.fout.write("<td>%s</td>" % data['url'])
                self.fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
                self.fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
                self.fout.write("</tr>")
            except:
                ""
    def output_self_html(self):
        self.output_html(self.datas)
        self.init_end()
    
    def output_row(self, dataset):
        for data in dataset:
            try:
                self.fout.write("<tr>")
                self.fout.write("<td>%s</td>" % data)
                #self.fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
                #self.fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
                self.fout.write("</tr>")
            except Exception,e:  
                print Exception,":",e
    def init_end(self):
        self.fout.write("</table>")
        self.fout.write("</body>")
        self.fout.write("</html>")
        self.fout.close()
    
    
    
    



