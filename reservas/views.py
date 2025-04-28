from django.shortcuts import render


def home(request):
    return render(request, 'tempReservas/index.html')

def buscar_reserva(request):
    # lógica futura
    return render(request, 'tempReservas/resultados.html')