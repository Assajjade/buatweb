import numpy as np
from django.shortcuts import render

def show_main(request):
  
    return render(request, "Beranda.html")

def show_Panduan(request):

    return render(request, "Panduan.html")

def show_Lokal(request):

    # Data dan fitting polinomial

    x = np.array([22.035, 32.33, 40.585, 53.635, 62.1])
    y = np.array([0.101787, 0.046856, 0.03666, 0.0176, 0.01217])
    degree = 2
    p = np.polyfit(x, np.log(y), degree)
    p[-1] = 0
    b = 0.01;

    x_extended = np.linspace(0, 120, 200)
    y_extended_fit = np.exp(np.polyval(p, x_extended))

    index = np.argmin(np.abs(y_extended_fit - b))
    x_value = x_extended[index]

    print("Nilai x_extended yang sesuai adalah:", x_value)
    # Create your views here.
    context = {
        'name': 'Pak Bepe',
        'Nilai_x': x_value,
    }

    return render(request, "Lokal.html", context)

def show_Pr(request):

    return render(request, "PR.html")

def show_Primary(request):

    return render(request, "Primary.html")

def show_Sec(request):

    return render(request, "Sec.html")

def form(request):
    x = np.array([22.035, 32.33, 40.585, 53.635, 62.1])
    y = np.array([0.101787, 0.046856, 0.03666, 0.0176, 0.01217])
    degree = 2
    p = np.polyfit(x, np.log(y), degree)
    p[-1] = 0
    b = 0.01;

    if request.method == 'POST':
        b = float(request.POST.get('masukan'))
        if b <= 0.00680943:
            context = {
            'Nilai_x': "ERROR",
            }
            return render(request, "Lokal.html", context)
        x_extended = np.linspace(0, 120, 200)
        y_extended_fit = np.exp(np.polyval(p, x_extended))

        index = np.argmin(np.abs(y_extended_fit - b))
        x_value = x_extended[index]

        print("Nilai x_extended yang sesuai adalah:", b)
        # Create your views here.
        context = {
            'Nilai_x': x_value,
        }
        return render(request, "Lokal.html", context)

    x_extended = np.linspace(0, 120, 200)
    y_extended_fit = np.exp(np.polyval(p, x_extended))

    index = np.argmin(np.abs(y_extended_fit - b))
    x_value = x_extended[index]

    print("Nilai x_extended yang sesuai adalah:", x_value)
    # Create your views here.
    context = {
        'Nilai_x': x_value,
    }
    
        
    return render(request, "Lokal.html", context)