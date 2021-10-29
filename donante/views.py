from django.shortcuts import render, redirect, get_object_or_404
from donante.models import Donante
from donante.forms import *
from django.core.mail import send_mail

# Create your views here.

def donantes(request):
    donantes = Donante.objects.all().order_by('-created')
    form = donanteFormulario()

    messageSuccess = []
    messageError = []
        
    #Reportar
    if request.method == "POST":        
        if (request.POST.get('reportar')):            
            try:
                idDonante = get_object_or_404(Donante, id=request.POST.get('idDonante'))
                if idDonante.cantidadReportado is None:
                    idDonante.cantidadReportado = 1                
                else:
                    idDonante.cantidadReportado = idDonante.cantidadReportado + 1
                idDonante.save() 
                request.session['successR'] = 'successR'
                if idDonante.cantidadReportado >= 10:                          
                    send_mail('Reporte de donante', 'Veces que el ID '+ str(request.POST.get('idDonante') + request.POST.get('idDonante') + " se ha reportado: " + str(idDonante.cantidadReportado)), 'from@example.com', ['juanko682@gmail.com', 'dagomez.9706@gmail.com'],fail_silently = False,)                                             
                return redirect('/donante/')
            except:                
                request.session['errorR'] = 'errorR'
                return redirect('/donante/')               

        #Agregar
        if (request.POST.get('add')):            
            tipoSangre=['A+','A-','B+','B-','AB+','AB-','O+','O-']
            transporte=['Si','No']
            if ((request.POST.get('tipoDeSangre') in tipoSangre) and (request.POST.get('poseeTransporte') in transporte) and (len(request.POST.get('telefonoContacto')) == 8)):
                print(dict(request.POST))
                d = Donante(nombre=str(request.POST.get('nombre')),                 
                tipoDeSangre=str(request.POST.get('tipoDeSangre')),
                poseeTransporte=str(request.POST.get('poseeTransporte')),
                informacionAdicional=str(request.POST.get('informacionAdicional')),
                telefonoContacto=str(request.POST.get('telefonoContacto')),
                cantidadReportado='0')
                try:
                    d.save()
                    messageSuccess.append("Registro agregado")
                    request.session['success'] = 'success'
                    return redirect('/donante/')
                except:    
                    request.session['error'] = 'error'                
                    return redirect('/donante/')                                       
            else:
                request.session['error'] = 'error'                
                return redirect('/donante/')               

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

    context = {
        'donantes': donantes,
        'form': form,
        'messageError' : messageError,  
        'messageSuccess' : messageSuccess,
    }

    return render(request, "donante/donante.html", context)
    