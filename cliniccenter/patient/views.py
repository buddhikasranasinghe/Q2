from datetime import datetime
from django.shortcuts import render, redirect
from .models import Patient
from .models import Prescription

# Create your views here.

def add_patient(request):
    if request.method == 'GET':
        return render(request, 'patient/addpatient.html')
    else:
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        birthdate = request.POST.get('bday')
        contactnumber = request.POST.get('cno')
        profileimage = request.POST.get('pimg')
        nicnumber = request.POST.get('nic')
        specialnotes = request.POST.get('notes')
        
        patient = Patient(f_name = firstname, l_name = lastname, birthday = birthdate, contactno = contactnumber, photo = profileimage, nic = nicnumber, notes = specialnotes)
        patient.save()
        
        return redirect('/patient')

def patient_details(request):
    if request.method == "GET":
        usernic = request.GET.get('snic')
        userresult = Patient.objects.filter(nic=usernic)
        if userresult:
            userpresciptions = Prescription.objects.filter(patient=userresult[0].id)
            context = {'userdetails':userresult, 'presciptiondetails':userpresciptions}
            return render(request, 'patient/details.html', context)
        else:
            context = {'message': 'Patient Not Found !!'}
            return render(request, 'patient/details.html', context)
    else:
        return render(request, 'patient/details.html')

def add_prescription(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        context = {'patients': patients}
        return render(request, 'patient/prescription.html', context)
    else:
        patientid = request.POST.get('patient')
        totalamount = request.POST.get('amount')
        currentdate = datetime.today()
        note = request.POST.get('notes')
        
        prescription = Prescription(patient=Patient.objects.get(id=patientid), prescription= note, amount = totalamount, date = currentdate)
        prescription.save()
        
        return redirect('/patient')

def revenue_details(request):
    if request.method == 'GET':
        return render(request, 'patient/revenue.html')
    else:
        start = request.POST.get('from')
        end = request.POST.get('to')
        result = Prescription.objects.filter(date__range=[start, end])
        totalRevenue = 0
        for rev in result:
            totalRevenue += rev.amount
        context = {'revenue': totalRevenue, 'from': start, 'to':end}
        
        return render(request, 'patient/revenue.html', context)
