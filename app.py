import streamlit as st
import numpy as np

import pickle



pipe=pickle.load(open('pipe.pkl','rb'))

df=pickle.load(open('df.pkl','rb'))


st.title("Laptop Price Predictor")

comapany= st.selectbox('brand',df["Company"].unique())    ##


type=st.selectbox('type',df["TypeName"].unique())  ##

ram=st.selectbox('Ram(in GB)',df["Ram"].unique())

weight=st.number_input("enter the weight of laptop")   

touchscreen=st.selectbox('Touchscreen',["Yes","No"])  ##

ips=st.selectbox('IPS',["Yes","No"])###


screen_size = st.number_input('Screen Size')

# resolution

resolution = st.selectbox ('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440','2304x1440'])

cpu_brand= st.selectbox('Cpu_brand',df["cpu brand"].unique())

gpu_brand= st.selectbox('Gpu_brand',df["Gpu brand"].unique())

os= st.selectbox('OS',df["os"].unique())

ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])


if st.button("Predict Price"):
    
    resolutionx=int(resolution.split("x")[0])
    resolutiony=int(resolution.split("x")[1])
    
    ppi=(((resolutionx**2)+(resolutiony**2))**0.5)/screen_size
    if touchscreen=="yes":
        touchscreen=1
    else:
        touchscreen=0
        
    if ips=="yes":
        ips=1
        
    else:
        ips=0
    
    
    query=np.array([comapany,type,ram,weight,touchscreen,ips,ppi,cpu_brand,gpu_brand,os,ssd,hdd])
    query=query.reshape(1,12)
    
    
                    
    st.title("The predicted price of this configuration is "+str(int(np.exp(pipe.predict(query))[0])))