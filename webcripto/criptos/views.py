import datetime
from tkinter.messagebox import Message
from django.shortcuts import render, redirect
from .models import Cripto
from .forms import CriptoForm
import django_excel as excel

def home(request):
    return render(request,'pages/home.html')

def quiensoy(request):
    return render(request,'pages/quiensoy.html')

def criptos(request):
    #lectura de base de datos
    criptos= Cripto.objects.all()
    print(criptos)
    return render(request,'criptos/index.html',{'criptos': criptos})

def create(request):
    formulario=CriptoForm(request.POST or None, request.FILES or None)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('criptos')
        
    return render(request,'criptos/create.html', {'formulario':formulario})

def update(request, id):
    cripto=Cripto.objects.get(id=id)
    formulario=CriptoForm(request.POST or None, request.FILES or None, instance=cripto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('criptos')
    
    return render(request,'criptos/update.html', {'formulario':formulario})

def getById(request, id):
    #lectura de base de datos
    criptoId= Cripto.objects.get(id=id)
    formulario=CriptoForm(request.POST or None, request.FILES or None, instance=criptoId)
    if formulario.is_valid() and request.POST:
        return redirect('criptos')
    
    return render(request,'criptos/criptoGet.html', {'formulario':formulario})

def delete(request, id):
     criptoId= Cripto.objects.get(id=id)
     criptoId.delete()
     return redirect('criptos')

def excelResult(request):
    export = []
    # Se agregan los encabezados de las columnas
    export.append(['Moneda', 'Unidades'])
    
    
    # Se obtienen los datos de la tabla o model y se agregan al array
    results = Cripto.objects.all()
    for result in results:
        # ejemplo para dar formato a fechas, estados (si/no, ok/fail) o
        # acceder a campos con relaciones y no solo al id
        export.append([
                result.sigle,
                result.unids,
                ])

    # Obtenemos la fecha para agregarla al nombre del archivo
    
    

    # se transforma el array a una hoja de calculo en memoria
    sheet = excel.pe.Sheet(export)

    # se devuelve como "Response" el archivo para que se pueda "guardar"
    # en el navegador, es decir como hacer un "Download"
    return excel.make_response(sheet, "csv", file_name="Criptomonedas.csv")