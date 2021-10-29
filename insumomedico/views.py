from django.shortcuts import render, redirect
from .models import InsumoMedico
from .forms import InsumoMedicoForm
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your views here.

def insumosmedicos(request):    
    insumosmedicos = InsumoMedico.objects.all().order_by('-created')
    messageSuccess = []
    messageError = []
    context = {        
        'insumosmedicos': insumosmedicos,
        'messageError' : messageError,  
        'messageSuccess' : messageSuccess,
    }   
    
    if request.method == "POST":
        if request.POST.get('nombreEstablecimiento') and request.POST.get('informacionAdicional'):    
            e = InsumoMedico(nombreEstablecimiento=request.POST.get('nombreEstablecimiento'),sitio=request.POST.get('sitio'),informacionAdicional=request.POST.get('informacionAdicional'))                                         
            guardar = True
            if request.POST.get('sitio'):
                validator = URLValidator()
                try:                    
                    validator(request.POST.get('sitio'))                    
                except ValidationError:                    
                    guardar = False                                        
            if guardar:                
                try:                     
                    request.session['success'] = 'success'                   
                    e.save()
                    return redirect('/insumomedico/')                                                              
                except:                                                   
                    request.session['error'] = 'error'                                    
            else:            
                request.session['error1'] = 'error1'
                return redirect('/insumomedico/')                                         
        else:            
            messageError.append("Debe completar el formulario")

    if 'success' in request.session:
        messageSuccess.append("Registro agregado")
        del request.session['success']
    
    if 'error' in request.session:
        messageError.append("Error al registrar") 
        del request.session['error']
    
    if 'error1' in request.session:
        messageError.append("URL errónea") 
        del request.session['error1']
    
    return render(request, "insumomedico/insumomedico.html", context)