
import pandas as pd
import numpy as np
import streamlit as st

def get_code1(link):
    marketId1=link.split('"',1)
    marketId1=marketId1[1]
    marketId1=marketId1.split('"',1)
    marketId1=marketId1[0]
    
    selectionId1=link.split('selectionId: ',1)
    selectionId1=selectionId1[1]
    selectionId1=selectionId1.split('}',1)
    selectionId1s=selectionId1[0]
    link2=selectionId1[1]

    code1=marketId1+"|"+selectionId1s
    
    
    code=code1+"|SIMPLE_SELECTION|%0A"
    return(code)

def get_code2(link):
    marketId1=link.split('"',1)
    marketId1=marketId1[1]
    marketId1=marketId1.split('"',1)
    marketId1=marketId1[0]
    
    selectionId1=link.split('selectionId: ',1)
    selectionId1=selectionId1[1]
    selectionId1=selectionId1.split('}',1)
    selectionId1s=selectionId1[0]
    link2=selectionId1[1]

    code1=marketId1+"|"+selectionId1s
    
    marketId2=link2.split('"',1)
    marketId2=marketId2[1]
    marketId2=marketId2.split('"',1)
    marketId2=marketId2[0]
    
    selectionId2=link2.split('selectionId: ',1)
    selectionId2=selectionId2[1]
    selectionId2=selectionId2.split('}',1)
    selectionId2s=selectionId2[0]
    link3=selectionId2[1]

    code2=marketId2+"|"+selectionId2s
    
    
    code=code1+"|SIMPLE_SELECTION|%26leg%3D"+code2+"|SIMPLE_SELECTION|%0A"
    return(code)

def get_code3(link):
    marketId1=link.split('"',1)
    marketId1=marketId1[1]
    marketId1=marketId1.split('"',1)
    marketId1=marketId1[0]
    
    selectionId1=link.split('selectionId: ',1)
    selectionId1=selectionId1[1]
    selectionId1=selectionId1.split('}',1)
    selectionId1s=selectionId1[0]
    link2=selectionId1[1]

    code1=marketId1+"|"+selectionId1s
    
    marketId2=link2.split('"',1)
    marketId2=marketId2[1]
    marketId2=marketId2.split('"',1)
    marketId2=marketId2[0]
    
    selectionId2=link2.split('selectionId: ',1)
    selectionId2=selectionId2[1]
    selectionId2=selectionId2.split('}',1)
    selectionId2s=selectionId2[0]
    link3=selectionId2[1]

    code2=marketId2+"|"+selectionId2s
    
    marketId3=link3.split('"',1)
    marketId3=marketId3[1]
    marketId3=marketId3.split('"',1)
    marketId3=marketId3[0]
    
    selectionId3=link3.split('selectionId: ',1)
    selectionId3=selectionId3[1]
    selectionId3=selectionId3.split('}',1)
    selectionId3s=selectionId3[0]
    link4=selectionId3[1]

    code3=marketId3+"|"+selectionId3s
    
    code=code1+"|SIMPLE_SELECTION|%26leg%3D"+code2+"|SIMPLE_SELECTION|%26leg%3D"+code3+"|SIMPLE_SELECTION|%0A"
    return(code)

def get_code4(link):
    marketId1=link.split('"',1)
    marketId1=marketId1[1]
    marketId1=marketId1.split('"',1)
    marketId1=marketId1[0]
    
    selectionId1=link.split('selectionId: ',1)
    selectionId1=selectionId1[1]
    selectionId1=selectionId1.split('}',1)
    selectionId1s=selectionId1[0]
    link2=selectionId1[1]

    code1=marketId1+"|"+selectionId1s
    
    marketId2=link2.split('"',1)
    marketId2=marketId2[1]
    marketId2=marketId2.split('"',1)
    marketId2=marketId2[0]
    
    selectionId2=link2.split('selectionId: ',1)
    selectionId2=selectionId2[1]
    selectionId2=selectionId2.split('}',1)
    selectionId2s=selectionId2[0]
    link3=selectionId2[1]

    code2=marketId2+"|"+selectionId2s
    
    marketId3=link3.split('"',1)
    marketId3=marketId3[1]
    marketId3=marketId3.split('"',1)
    marketId3=marketId3[0]
    
    selectionId3=link3.split('selectionId: ',1)
    selectionId3=selectionId3[1]
    selectionId3=selectionId3.split('}',1)
    selectionId3s=selectionId3[0]
    link4=selectionId3[1]

    code3=marketId3+"|"+selectionId3s
    
    marketId4=link4.split('"',1)
    marketId4=marketId4[1]
    marketId4=marketId4.split('"',1)
    marketId4=marketId4[0]
    
    selectionId4=link4.split('selectionId: ',1)
    selectionId4=selectionId4[1]
    selectionId4=selectionId4.split('}',1)
    selectionId4s=selectionId4[0]
    link5=selectionId4[1]

    code4=marketId4+"|"+selectionId4s
    
    
    code=code1+"|SIMPLE_SELECTION|%26leg%3D"+code2+"|SIMPLE_SELECTION|%26leg%3D"+code3+"|SIMPLE_SELECTION|%26leg%3D"+code4+"|SIMPLE_SELECTION|%0A"
    return(code)

def get_code5(link):
    marketId1=link.split('"',1)
    marketId1=marketId1[1]
    marketId1=marketId1.split('"',1)
    marketId1=marketId1[0]
    
    selectionId1=link.split('selectionId: ',1)
    selectionId1=selectionId1[1]
    selectionId1=selectionId1.split('}',1)
    selectionId1s=selectionId1[0]
    link2=selectionId1[1]

    code1=marketId1+"|"+selectionId1s
    
    marketId2=link2.split('"',1)
    marketId2=marketId2[1]
    marketId2=marketId2.split('"',1)
    marketId2=marketId2[0]
    
    selectionId2=link2.split('selectionId: ',1)
    selectionId2=selectionId2[1]
    selectionId2=selectionId2.split('}',1)
    selectionId2s=selectionId2[0]
    link3=selectionId2[1]

    code2=marketId2+"|"+selectionId2s
    
    marketId3=link3.split('"',1)
    marketId3=marketId3[1]
    marketId3=marketId3.split('"',1)
    marketId3=marketId3[0]
    
    selectionId3=link3.split('selectionId: ',1)
    selectionId3=selectionId3[1]
    selectionId3=selectionId3.split('}',1)
    selectionId3s=selectionId3[0]
    link4=selectionId3[1]

    code3=marketId3+"|"+selectionId3s
    
    marketId4=link4.split('"',1)
    marketId4=marketId4[1]
    marketId4=marketId4.split('"',1)
    marketId4=marketId4[0]
    
    selectionId4=link4.split('selectionId: ',1)
    selectionId4=selectionId4[1]
    selectionId4=selectionId4.split('}',1)
    selectionId4s=selectionId4[0]
    link5=selectionId4[1]

    code4=marketId4+"|"+selectionId4s
    
    marketId5=link5.split('"',1)
    marketId5=marketId5[1]
    marketId5=marketId5.split('"',1)
    marketId5=marketId5[0]
    
    selectionId5=link5.split('selectionId: ',1)
    selectionId5=selectionId5[1]
    selectionId5=selectionId5.split('}',1)
    selectionId5s=selectionId5[0]
    link6=selectionId5[1]

    code5=marketId5+"|"+selectionId5s
    
    marketId6=link6.split('"',1)
    marketId6=marketId6[1]
    marketId6=marketId6.split('"',1)
    marketId6=marketId6[0]
    
    
    code=code1+"|SIMPLE_SELECTION|%26leg%3D"+code2+"|SIMPLE_SELECTION|%26leg%3D"+code3+"|SIMPLE_SELECTION|%26leg%3D"+code4+"|SIMPLE_SELECTION|%26leg%3D"+code5+"|SIMPLE_SELECTION|%0A"
    return(code)

def get_code6(link):
    marketId1=link.split('"',1)
    marketId1=marketId1[1]
    marketId1=marketId1.split('"',1)
    marketId1=marketId1[0]
    
    selectionId1=link.split('selectionId: ',1)
    selectionId1=selectionId1[1]
    selectionId1=selectionId1.split('}',1)
    selectionId1s=selectionId1[0]
    link2=selectionId1[1]

    code1=marketId1+"|"+selectionId1s
    
    marketId2=link2.split('"',1)
    marketId2=marketId2[1]
    marketId2=marketId2.split('"',1)
    marketId2=marketId2[0]
    
    selectionId2=link2.split('selectionId: ',1)
    selectionId2=selectionId2[1]
    selectionId2=selectionId2.split('}',1)
    selectionId2s=selectionId2[0]
    link3=selectionId2[1]

    code2=marketId2+"|"+selectionId2s
    
    marketId3=link3.split('"',1)
    marketId3=marketId3[1]
    marketId3=marketId3.split('"',1)
    marketId3=marketId3[0]
    
    selectionId3=link3.split('selectionId: ',1)
    selectionId3=selectionId3[1]
    selectionId3=selectionId3.split('}',1)
    selectionId3s=selectionId3[0]
    link4=selectionId3[1]

    code3=marketId3+"|"+selectionId3s
    
    marketId4=link4.split('"',1)
    marketId4=marketId4[1]
    marketId4=marketId4.split('"',1)
    marketId4=marketId4[0]
    
    selectionId4=link4.split('selectionId: ',1)
    selectionId4=selectionId4[1]
    selectionId4=selectionId4.split('}',1)
    selectionId4s=selectionId4[0]
    link5=selectionId4[1]

    code4=marketId4+"|"+selectionId4s
    
    marketId5=link5.split('"',1)
    marketId5=marketId5[1]
    marketId5=marketId5.split('"',1)
    marketId5=marketId5[0]
    
    selectionId5=link5.split('selectionId: ',1)
    selectionId5=selectionId5[1]
    selectionId5=selectionId5.split('}',1)
    selectionId5s=selectionId5[0]
    link6=selectionId5[1]

    code5=marketId5+"|"+selectionId5s
    
    marketId6=link6.split('"',1)
    marketId6=marketId6[1]
    marketId6=marketId6.split('"',1)
    marketId6=marketId6[0]
    
    selectionId6=link6.split('selectionId: ',1)
    selectionId6=selectionId6[1]
    selectionId6=selectionId6.split('}',1)
    selectionId6s=selectionId6[0]
    link7=selectionId5[1]

    code6=marketId6+"|"+selectionId6s
    
    code=code1+"|SIMPLE_SELECTION|%26leg%3D"+code2+"|SIMPLE_SELECTION|%26leg%3D"+code3+"|SIMPLE_SELECTION|%26leg%3D"+code4+"|SIMPLE_SELECTION|%26leg%3D"+code5+"|SIMPLE_SELECTION|%26leg%3D"+code6+"|SIMPLE_SELECTION|%0A"
    return(code)

st.title(f"Paddy Power betslip link creator")

selections = [1,2,3,4,5,6]
acca = st.sidebar.selectbox(
    "Choose number of selections in acca:", selections, index=0)

link1 = st.sidebar.text_input('Enter raw code from Paddy Power')

if link1 is not '':
    link1=link1
else:
    st.write("You must enter the raw code from Paddy Power")
    st.stop()

if acca ==1:
    final_link=get_code1(link1)
elif acca ==2:
    final_link=get_code2(link1)
elif acca ==3:
    final_link=get_code3(link1)
elif acca ==4:
    final_link=get_code4(link1)
elif acca ==5:
    final_link=get_code5(link1)
else:
    final_link=get_code6(link1)

PIDcode=st.sidebar.text_input('Enter PID')
if PIDcode is not '':
    PIDcode=PIDcode
else:
    st.write("You must enter a PID")
    st.stop()
    
prelink='https://media.paddypower.com/redirect.aspx?pid='+PIDcode+'&bid=7049&redirectURL=https://www.paddypower.com/bet%3Faction%3DaddLegs%26leg%3D'



st.write(prelink+final_link)



#if link1 is not '':
 #   code1=get_code(link1)
#else:
 #   st.write("You must add at least one link")
  #  st.stop()
