from django.shortcuts import render, HttpResponse, redirect
from cWeb.models import *
from django.utils import timezone
import pandas as pd
from weasyprint import HTML
import win32print



def home(request):
    if request.method == "POST":
        fullName = request.POST['fullName']    
        phoneNumber = request.POST['phoneNumber']    
        age = int(request.POST['age'])    
        bloodPressure = request.POST['bloodPressure']    
        tempreture = request.POST['tempreture']  

        varInput = int(request.POST['varInput'])
        
        dose = [0,'OPD', 'TPD', 'THPD']

        cust,created = Customer_record.objects.update_or_create(fullName=fullName, age=age, phoneNumber=phoneNumber)
        # Medicine_pres(customerId=cust, )


        for i in range(1,int(varInput)+1):

            Medicine_pres.objects.create(customerId=cust, medName= Medicine_record.objects.get(medName=request.POST[f"med{i}"]) , dose=1)
            

        html = '<html><body><h1>Hello, world!</h1></body></html>'
        pdf = HTML(string=html).write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="file.pdf"'
        return response

        
    return render(request, 'home.html', context={"varInput":0, 'medicines':Medicine_record.objects.all()})


def medicines(request):

    if request.method == 'POST' and request.FILES.get('file'):
       
            # Get the uploaded file
        file = request.FILES['file']

        # Load the data from the Excel file using pandas
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            if Medicine_record.objects.filter(medName=row['Name']).exists():
                med = Medicine_record.objects.get(medName=row['Name'])
            else:
                med =Medicine_record.objects.create(medName=row['Name'], currentStock=0, price=0,lastLoadedStock=0)
            med.currentStock += row['Quantity']
            med.price = row['Price']
            med.lastLoadedStock = row['Quantity']
            med.save()

    elif request.method == "POST":
        counter = int(request.POST['counter'])

        for i in range(1, counter+1):
            med = Medicine_record.objects.get(medName=request.POST[f'name{i}'])
            med.currentStock += int(request.POST[f'stock{i}'])
            med.price = int(request.POST[f'price{i}'])
            med.lastLoadedStock = int(request.POST[f'stock{i}'])
            med.save()


    return render(request, 'medicines.html', context={'medicines':Medicine_record.objects.all(), 
    'todayDate':timezone.now()})


def customers(request):
    return render(request, 'patients.html', context={'customers':Customer_record.objects.all()})



def profile(request, profileID):
    if (profileID):
        obj = Customer_record.objects.get(pk=profileID)
        context = {
            "cust" :obj,
            "medicines" :Medicine_pres.objects.filter(customerId=obj)
        }
        return render(request, 'profile.html', context=context)


def insights(request):

    return render(request, 'insights.html', context={"customers":customers(request)})



