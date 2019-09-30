import datetime
import sys
import socket
import string
import time
from time import strftime
HOST="xxx.yyy.www.zzz" #aca va la ip del server
PORT=6666
NICK="esclavo_01" #aca va el nombre del bot
IDENT="root"
REALNAME="root"
readbuffer=""
timestamp=""
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN #channel\r\n")
while 1:
 readbuffer=readbuffer+s.recv(2048)
 print readbuffer
 rb=readbuffer
 timestamp=strftime("%Y-%m-%d %H:%M:%S")
 if rb.find("PING")<0:
 archi2=open('/var/www/html/irc/irc_bot_log.txt','a')
 archi2.write(timestamp+":"+rb+'\n')
 archi2.close()
 #SI EL MENSAJE CONTIENE UN JOIN Y EL SEPARADOR "!" ESTA EN LA POS 6
 if readbuffer.find("JOIN")>=0 and readbuffer[6:7]=="!":
 #timestamp=datetime().now().strftime("%Y-%m-%d %H:%M")
 #timestamp = strftime("%Y-%m-%d %H:%M:%S")
 #timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
 #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 str="PRIVMSG "+readbuffer[1:6]+" :-ip\n"
 s.send(str)
 str=""
 print timestamp
 temp=string.split(readbuffer, "\n")
 readbuffer=temp.pop( )
 for line in temp:
 line=string.rstrip(line)
 line=string.split(line)
 if line[1]=="PRIVMSG" and line[2]==NICK:
 name=rb[1:6]
 #str2="PRIVMSG "+name+" :"+timestamp+" -les traigo paz\n"
 #s.send(str2)
 if(line[0]=="PING"):
 s.send("PONG %s\r\n" % line[1])