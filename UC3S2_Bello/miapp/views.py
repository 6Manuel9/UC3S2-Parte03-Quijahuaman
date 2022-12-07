from django.shortcuts import render
index = """
    <h1>Proyecto web (LP3) Henry Carrasco </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/primos/a/b"> Mostrar Números </a>
        </li>
    </ul>
"""

def index(request):
    return render(request, 'index.html')
def inicio(request):
    return render(request, 'inicio.html')
def es_primo(requets,num):
    
    for i in range(2,num):
        if num%i==0:
        return False
    return True
    
def primos(requets,a,b):
    if a>b:
        return redirect('primos',a=b,b=a)
    cont = f"""
        <h2> Numeros de [{a}, {b}]</h2>
        Resultado: <br>
        <u1>
    """"
    for i in range(a,b):
        if es_primo(i) == True:
            cont += 1
            print i
        print ""
        print cont "</u1>"
    return HttpResponse(layout + cont)
# Create your views here.
