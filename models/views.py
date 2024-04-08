from django.shortcuts import render

# Create your views here.
vehicles=[]

def cars(request):
    if request.method=="POST":
        name=request.POST.get('brand')
        model=request.POST.get('model')
        speed=request.POST.get('speed')
        fuel=request.POST.get('fuel')
        gear=request.POST.get('gear')
        color=request.POST.get('color')
        price=request.POST.get('price')
        vehicles.append({"Brand":name,"Model":model,"Speed":speed,"Fuel_Type":fuel,"Gear_System":gear,"Colour":color,"Price":price})
        return render(request,'index.html',{'data':vehicles})
    else:
        return render(request,'index.html',{'data':vehicles})

    
        
    

    
    
