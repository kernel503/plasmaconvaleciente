from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm
from django.core.mail import send_mail
from paciente.listado import *

# Create your views here.

def pacientes(request):
    pacientes = Paciente.objects.all().order_by('-created')
    messageSuccess = []
    messageError = []
    form = PacienteForm()
    context = {
        'form': form,
        'pacientes': pacientes,
        'messageError' : messageError,  
        'messageSuccess' : messageSuccess,
    }

    #Reportar
    if request.method == "POST":
        if (request.POST.get('reportar')):                    
            try:
                idPaciente = get_object_or_404(Paciente, id=request.POST.get('idPaciente'))                              
                if idPaciente.cantidadReportado is None:
                    idPaciente.cantidadReportado = 1                
                else:
                    idPaciente.cantidadReportado = idPaciente.cantidadReportado + 1                
                idPaciente.save()
                request.session['successR'] = 'successR'                                                 
                if idPaciente.cantidadReportado >= 10:                      
                    send_mail('Reporte de paciente', 'Veces que el ID '+ str(request.POST.get('idPaciente') + " se ha reportado: " + str(idPaciente.cantidadReportado)), 'from@example.com', ['juanko682@gmail.com', 'dagomez.9706@gmail.com'],fail_silently = False,)                                 
                return redirect('/paciente/')    
            except:                                  
                request.session['errorR'] = 'errorR'
                return redirect('/paciente/')
                
    #Agregar
    if request.method == "POST": 
        print(dict(request.POST))  
        if (request.POST.get('add')):  
            try:                          
                if request.POST.get('tipoDeSangre') in dict(getSangre()) and request.POST.get('nombre') and request.POST.get('hospital') and request.POST.get('informacionAdicional'):
                    p = Paciente(nombre=request.POST.get('nombre'), 
                    tipoDeSangre=request.POST.get('tipoDeSangre'),
                    hospital=request.POST.get('hospital'),
                    informacionAdicional=request.POST.get('informacionAdicional'),
                    cantidadReportado=0)
                    p.save()                   
                    request.session['success'] = 'success'
                    return redirect('/paciente/')            
                else:                                     
                    request.session['error'] = 'error'
                    return redirect('/paciente/')                                    
            except:                
                request.session['error'] = 'error'
                return redirect('/paciente/')                 
    
    if 'success' in request.session:
        messageSuccess.append("Registro agregado")
        del request.session['success']
    
    if 'error' in request.session:
        messageError.append("Error al registrar") 
        del request.session['error']

    if 'errorR' in request.session:
        messageError.append("Error al reportar")
        del request.session['errorR']
    
    if 'successR' in request.session:
        messageSuccess.append("Registro reportado")
        del request.session['successR']

    return render(request, "paciente/paciente.html", context)