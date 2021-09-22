import pandas as pd
import numpy as np
import streamlit as st


def get_code(link):
    bssId1=link.split('&bssId=',1)
    bssId1=bssId1[1]
    bssId1=bssId1.rsplit('&bsmSt',1)
    bssId1=bssId1[0]
    
    bsmId1=link.split('&bsmId=',1)
    bsmId1=bsmId1[1]
    bsmId1=bsmId1.rsplit('&modules',1)
    bsmId1=bsmId1[0]

    code=bsmId1+"|"+bssId1
    return(code)


PIDcode=st.sidebar.text_input('Enter PID')

prelink='http://ads.betfair.com/redirect.aspx?pid='+PIDcode+'bid=9810&redirecturl=https://www.betfair.com/sport/betslip?bets='

link1 = st.sidebar.text_input('Enter link 1')
if link1 is not '':
    code1=get_code(link1)
else:
    st.write("You must add at least one link")
    st.stop()


link2 = st.sidebar.text_input('Enter link 2')
if link2 is not '':
     code2=get_code(link2)
else:
    st.write(prelink+code1)
    st.write("Input link 2 to make it a double")
    st.stop()

link3 = st.sidebar.text_input('Enter link 3')
if link3 is not '':
     code3=get_code(link3)
else:
    st.write(prelink+code1+";"+code2)
    st.write("Input link 3 to make it a treble")
    st.stop()
    
link4 = st.sidebar.text_input('Enter link 4')
if link4 is not '':
     code4=get_code(link4)
else:
    st.write(prelink+code1+";"+code2+";"+code3)
    st.write("Input link 4 to make it a 4-fold")
    st.stop()
    
link5 = st.sidebar.text_input('Enter link 5')
if link5 is not '':
     code5=get_code(link5)
else:
    st.write(prelink+code1+";"+code2+";"+code3+";"+code4)
    st.write("Input link 5 to make it a 5-fold")
    st.stop()
    
link6 = st.sidebar.text_input('Enter link 6')
if link6 is not '':
     code6=get_code(link6)
else:
    st.write(prelink+code1+";"+code2+";"+code3+";"+code4+";"+code5)
    st.write("Input link 6 to make it a 6-fold")
    st.stop()
    
link7 = st.sidebar.text_input('Enter link 7')
if link7 is not '':
     code7=get_code(link7)
else:
    st.write(prelink+code1+";"+code2+";"+code3+";"+code4+";"+code5+";"+code6)
    st.write("Input link 7 to make it a 7-fold")
    st.stop()
    
link8 = st.sidebar.text_input('Enter link 8')
if link8 is not '':
     code8=get_code(link8)
else:
    st.write(prelink+code1+";"+code2+";"+code3+";"+code4+";"+code5+";"+code6+";"+code7)
    st.write("Input link 8 to make it an 8-fold")
    st.stop()
    
link9 = st.sidebar.text_input('Enter link 9')
if link9 is not '':
     code9=get_code(link9)
else:
    st.write(prelink+code1+";"+code2+";"+code3+";"+code4+";"+code5+";"+code6+";"+code7+";"+code8)
    st.write("Input link 9 to make it a 9-fold")
    st.stop()
    
link10 = st.sidebar.text_input('Enter link 10')
if link10 is not '':
     code10=get_code(link10)
     st.write(prelink+code1+";"+code2+";"+code3+";"+code4+";"+code5+";"+code6+";"+code7+";"+code8+";"+code9+";"+code10)
else:
    st.write(prelink+code1+";"+code2+";"+code3+";"+code4+";"
             +code5+";"+code6+";"+code7+";"+code8+";"+code9)
    st.write("Input link 10 to make it a 10-fold")
    st.stop()
