#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we position two push
buttons in the bottom-right corner 
of the window. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
import os
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.l=QtGui.QTextEdit(self)
	self.l.setLineWrapMode(QtGui.QTextEdit.NoWrap)
	self.l.moveCursor(QtGui.QTextCursor.End)
	self.l.insertPlainText("#include<bits/stdc++.h> \n using namespace std;\n int main(){\n}")
	self.l.setGeometry(10,10,500,700)
	sb=self.l.verticalScrollBar()
	sb.setValue(sb.maximum()) 
	
	self.rt=QtGui.QTextEdit(self)
	self.rt.setLineWrapMode(QtGui.QTextEdit.NoWrap)
	self.rt.moveCursor(QtGui.QTextCursor.End)
	self.rt.insertPlainText("INPUT")
	self.rt.setGeometry(530,50,300,300)
	sb=self.rt.verticalScrollBar()
	sb.setValue(sb.maximum())

	self.rd=QtGui.QTextEdit(self)
	self.rd.setLineWrapMode(QtGui.QTextEdit.NoWrap)
	self.rd.moveCursor(QtGui.QTextCursor.End)
	self.rd.insertPlainText("OUTPUT")
	self.rd.setGeometry(530,400,300,300)
	sb=self.rd.verticalScrollBar()
	sb.setValue(sb.maximum())


	self.runButton = QtGui.QPushButton("run",self)
	self.runButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.runButton.setGeometry(620, 10, 70, 30)
        
        self.runButton.clicked.connect(self.onStart)
        
        self.setGeometry(200, 100, 900, 800)
        self.setWindowTitle('C++ compiler')    
        self.show()
    def onStart(self): 
	st=self.l.toPlainText()
	f=open("data.cpp","w")
	f.write(st)
	f.close()
	st=self.rt.toPlainText()
	f=open("input.txt","w")
	f.write(st)
	f.close()
	retvalue = os.system("g++ data.cpp > output.txt 2>&1")
	 
	if retvalue == 0:
	    retvalue = os.system("./a.out < input.txt > output.txt 2>&1")
	
	sttt=""
	with open("output.txt","r") as f:
	    st=f.read()
	    sttt=sttt+str(st)
	if retvalue==0:
	    self.rd.setPlainText(sttt)
	else :
	    print "jaypee"
	    self.rd.setPlainText(sttt)
	

    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

