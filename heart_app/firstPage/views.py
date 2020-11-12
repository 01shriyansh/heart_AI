from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pickle
import random 

reloadModel = pickle.load(open('./models/model4.pkl', 'rb'))

# Create your views here.
def index(request):
    temp={}
    temp['age']=request.POST.get('age')
    temp['sex']=request.POST.get('gender')
    temp['cp']=request.POST.get('cp')
    temp['trestbps']=request.POST.get('trestbps')
    temp['chol']=request.POST.get('chol')
    temp['fbs']=request.POST.get('fbs')
    temp['restecg']=request.POST.get('restecg')
    temp['thalach']=request.POST.get('thalach')
    temp['exang']=request.POST.get('exang')
    temp['oldpeak']=request.POST.get('oldpeak')
    temp['slope']=request.POST.get('slope')
    temp['ca']=request.POST.get('ca')
    temp['thal']=request.POST.get('thal')
    context={'temp':temp}
    return render(request,'index.html',context)
    # return HttpResponse()

def predictheart(request):
    name_patient=""
    if request.method == 'POST':
        temp={}
        name_patient=request.POST.get('name_p')
        temp['age']=request.POST.get('age')
        temp['sex']=request.POST.get('gender')
        temp['cp']=request.POST.get('cp')
        temp['trestbps']=request.POST.get('trestbps')
        temp['chol']=request.POST.get('chol')
        temp['fbs']=request.POST.get('fbs')
        temp['restecg']=request.POST.get('restecg')
        temp['thalach']=request.POST.get('thalach')
        temp['exang']=request.POST.get('exang')
        temp['oldpeak']=request.POST.get('oldpeak')
        temp['slope']=request.POST.get('slope')
        temp['ca']=request.POST.get('ca')
        temp['thal']=request.POST.get('thal')

    testdata=pd.DataFrame({'x':temp}).transpose()
    scoreval=reloadModel.predict(testdata)[0]
    str1=f'{name_patient} you have a heart disease'
    str2=f'{name_patient} you do not have a heart disease . Still,'

    if scoreval==0:
        context={'scoreval':str2}
    else:
        context={'scoreval':str1}
    print("SCOREVAL",scoreval)
    return render(request,'index.html',context)

def booking(request):
    if request.method == 'POST':
        temp1={}
        temp1['name']=request.POST.get('name_p')
        temp1['phone']=request.POST.get('phone')
        temp1['date']=request.POST.get('date')

        time=request.POST.get('time')
        city=request.POST.get('city')
        hospital=request.POST.get('hospital')
        special=request.POST.get('special')

        print(type(time))
        if time == '1' :
            temp1['time']='8:00 - 8:30'
        elif time == '2':    
            temp1['time']='8:30 - 9:00'
        elif time == '3':
            temp1['time']='9:00 - 9:30'
        else:
            temp1['time']='9:30 - 10:00'

        if city == '1' :
            temp1['city']='Kota'
        elif city=='2':    
            temp1['city']='Jaipur'
        elif city=='3':
            temp1['city']='Jodhpur'
        else:
            temp1['city']='Ajmer'

        if hospital == 1 :
            temp1['hospital']='Fortis'
        elif hospital==2:    
            temp1['hospital']='Medcare'
        elif hospital==3:
            temp1['hospital']='Aiims'
        else:
            temp1['hospital']='Maxx'

        if special == 1 :
            temp1['special']='Dr. Ram'
        elif special==2:    
            temp1['special']='Dr. Shyam'
        elif special==3:
            temp1['special']='Dr. Sita'
        else:
            temp1['special']='Dr. Urmila'

        # temp1['time']=request.POST.get('time')
        # temp1['city']=request.POST.get('city')
        # temp1['hospital']=request.POST.get('hospital')
        # temp1['special']=request.POST.get('special')

        # temp1['time']=time
        # temp1['city']=city
        # temp1['hospital']=hospital
        # temp1['special']=special

        temp1['appo']=random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        book_context={'temp1':temp1}
    return render(request,'index.html',book_context)