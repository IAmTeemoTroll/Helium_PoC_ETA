# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:39:01 2021

@author: desmo_sxgiwmz
"""

import requests
import json 
import datetime
import tkinter as tk

box=[]
def sav_info():
    v1=f1.get()
    v2=l1.get()
    box.append(v1)
    box.append(v2)
    
    x=box[0]
    y=box[1]
    
    #x='112uUSEcHtQYskpVBcvnfuokoTmuJ2t2iCnyKE6wvUZQK5D9pjbW'
    #y=360
    
    t0='poc_challenge_interval =  '+str(y)+' blocks' 

    url="https://api.helium.io/v1/hotspots/"+x

    r=requests.get(url)
    cont=json.loads(r.content.decode())


    #last_poc_challenge
    p1=cont.get('data',{}).get('last_poc_challenge')
    t1='last_poc_challenge        =  '+str(p1)+' blocks'

    #last_change_block
    p2=cont.get('data',{}).get('last_change_block')
    t2='last_change_block         =  '+str(p2)+' blocks'

    #current_block
    p3=cont.get('data',{}).get('block')
    t3='block                               =  '+str(p3)+' blocks'

    #upcoming_poc_challenge
    diff=p1-p2
    d1='diff                                   =  '+ str(diff)+' blocks'

    p4=p1+y-diff
    t4='upcoming_poc              =  '+str(p4)+' blocks'

    #elapse_time_remainder
    p5=(p4-p3)/60
    t5='elapse_time                    =  '+'{:.2f}'.format(p5) + ' hours'

    #elapse_time_overall
    p6=y/60
    t6="{:.2f}".format(p6) + " hours"

    #progress_complete
    p7=((p6-p5)/p6) *100
    t7="{:.2f}".format(p7)+ " %"
    
    
    #time_conversion 

    def tc(time):
        hours=int(time)
        minutes=(time*60)%60
        seconds=(time*3600)%60
        return "%d:%02d:%02d" % (hours, minutes, seconds)


    p8=tc((p4-p3)/60)
    t8='                                        =  '+p8+ ' / ' +tc(y/60) + ' ('+t7+')'

    #current_time
    tm1=datetime.datetime.now()
    tm2="current_time                  =  "+tm1.strftime("%d/%m/%y %H:%M:%S")


    #final_time
    tmf1=tm1+datetime.timedelta(minutes=(p4-p3))
    tmf2="eta_next_poc                 =  "+tmf1.strftime("%d/%m/%y %H:%M:%S")

    text="\n"+t1+"\n"+t2+"\n"+d1+"\n\n" +t0+"\n\n"+t4+"\n"+t3+"\n\n"+t5+"\n"+t8+"\n\n"+tm2+"\n"+tmf2    
    

    myText.set(t1)
    myText2.set(t2)
    myText3.set(d1)
    myText4.set(t0)
    myText5.set(t4)
    myText6.set(t3)
    myText7.set(t5)
    myText8.set(t8)
    myText9.set(tm2)
    myText10.set(tmf2)
    
    print(v1,v2)

    
# open tkinter interface
root =tk.Tk()


#change GUID interface
length=500
width=450

root.geometry(str(length)+'x'+str(width))
root.title('Helium PoC Challenge')


#label
x1=50
y1=30

t1=tk.Label(root,text='Helium Miner Address').place(x=x1,y=y1,anchor='w')
t2=tk.Label(root,text='Blocks').place(x=x1,y=(y1*2)+20,anchor='w')
t3=tk.Label(root,text='Result').place(x=x1,y=(y1*4)+20,anchor='w')

#entry
f1=tk.StringVar()
l1=tk.IntVar()

myText=tk.StringVar()
myText2=tk.StringVar()
myText3=tk.StringVar()
myText4=tk.StringVar()
myText5=tk.StringVar()
myText6=tk.StringVar()
myText7=tk.StringVar()
myText8=tk.StringVar()
myText9=tk.StringVar()
myText10=tk.StringVar()



tk.Entry(root,textvariable=f1).place(x=x1+150,y=y1,anchor='w')
tk.Entry(root,textvariable=l1).place(x=x1+150,y=(y1*2)+20,anchor='w')

tk.Label(root,text="",textvariable=myText).place(x=x1+150,y=(y1*4)+20,anchor='w')
tk.Label(root,text="",textvariable=myText2).place(x=x1+150,y=(y1*4)+40,anchor='w')
tk.Label(root,text="",textvariable=myText3).place(x=x1+150,y=(y1*4)+60,anchor='w')
tk.Label(root,text="",textvariable=myText4).place(x=x1+150,y=(y1*4)+100,anchor='w')
tk.Label(root,text="",textvariable=myText5).place(x=x1+150,y=(y1*4)+120,anchor='w')
tk.Label(root,text="",textvariable=myText6).place(x=x1+150,y=(y1*4)+140,anchor='w')
tk.Label(root,text="",textvariable=myText7).place(x=x1+150,y=(y1*4)+160,anchor='w')
tk.Label(root,text="",textvariable=myText8).place(x=x1+150,y=(y1*4)+180,anchor='w')
tk.Label(root,text="",textvariable=myText9).place(x=x1+150,y=(y1*4)+220,anchor='w')
tk.Label(root,text="",textvariable=myText10).place(x=x1+150,y=(y1*4)+240,anchor='w')






#button 
tk.Button(text='Enter', width='10',command=sav_info).place(x=length-300,y=width-25,anchor='w')



root.mainloop()

