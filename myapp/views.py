from django.db.models.aggregates import Sum
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .form import *


# Create your views here.
def HomeView(request):
    creditform = CreditForm()
    debitform = DebitForm()
    transferform = TransferForm()
    fastbtnform = FastButtonForm()
    # Credit.
    credit_data = CreditModel.objects.all().order_by('-add_date')
    agg_credit = credit_data.aggregate(Sum('amt'))
    creditdata = [ i.amt for i in credit_data ]
    creditlbl = [ i.add_date.strftime("%m/%d/%Y, %H:%M:%S") for i in credit_data ]
    

    # Debit, 
    debit_data = DebitModel.objects.all().order_by('-add_date')
    agg_debit = debit_data.aggregate(Sum('amt')) 
    debitdata = [ i.amt for i in debit_data ]
    debitlbl = [ i.add_date.strftime("%m/%d/%Y, %H:%M:%S") for i in debit_data ]

    # Transfer data
    transfer_data = BankTransferModel.objects.all().order_by('-add_date') 
    agg_transfer = transfer_data.aggregate(Sum('amt'))  

    # Fast Button data
    fast_btn = CreditDebitTransferButtonModel.objects.all().order_by('amt') 
    context = {'creditform':creditform,'debitform':debitform,'transferform':transferform,'fastbtnform':fastbtnform,
    'credit_data':credit_data,'debit_data':debit_data,'transfer_data':transfer_data,'fast_btn':fast_btn,
    'agg_credit':agg_credit['amt__sum'],'agg_debit':agg_debit['amt__sum'],'agg_transfer':agg_transfer['amt__sum'],
    'creditdata': creditdata,'creditlbl': creditlbl,'debitdata':debitdata,'debitlbl':debitlbl}
    return render(request,'home.html',context)

def CreditSaveView(request):
    if request.method == 'POST':
        creditform = CreditForm(request.POST)
        if creditform.is_valid():
            amt = request.POST['amt']
            tag = request.POST['tag']
            crs = request.POST['csrfmiddlewaretoken']
            CreditModel(amt=amt,tag=tag).save()
            return JsonResponse({'status':'done'})
    
def DebitSaveView(request):
    if request.method == 'POST':
        debitform = DebitForm(request.POST)
        if debitform.is_valid():
            amt = request.POST['amt']
            tag = request.POST['tag']
            crs = request.POST['csrfmiddlewaretoken']
            DebitModel(amt=amt,tag=tag).save()
            return JsonResponse({'status':'done'})
    
def TransferSaveView(request):
    if request.method == 'POST':
        transferform = TransferForm(request.POST)
        if transferform.is_valid():
            amt = request.POST['amt']
            tag = request.POST['tag']
            crs = request.POST['csrfmiddlewaretoken']
            BankTransferModel(amt=amt,tag=tag).save()
            return JsonResponse({'status':'done'})
    
def GenerateFastButtonView(request):
    if request.method  == 'POST':
        form = FastButtonForm(request.POST)
        if form.is_valid():
            btn_amt = request.POST['amt']
            btn_tag = ['Fast Credit','Fast Debit','Fast Credit Transfer','Fast Debit Transfer']
            btn_type = request.POST['btn_type']
            crs = request.POST['csrfmiddlewaretoken']
            if btn_type == 'Credit':
                CreditDebitTransferButtonModel(amt=btn_amt,tag=btn_tag[0],btn_type=btn_type).save()
            if btn_type == 'Debit':
                CreditDebitTransferButtonModel(amt=btn_amt,tag=btn_tag[1],btn_type=btn_type).save()
            if btn_type == 'Credit Transfer':
                CreditDebitTransferButtonModel(amt=btn_amt,tag=btn_tag[2],btn_type=btn_type).save()
            if btn_type == 'Debit Transfer':
                CreditDebitTransferButtonModel(amt=btn_amt,tag=btn_tag[3],btn_type=btn_type).save()
            return JsonResponse({'status':'done'})
    


def FastButtonView(request):
    bid=request.GET.get("id")
    get_button=CreditDebitTransferButtonModel.objects.get(id=bid)
    if get_button.btn_type == 'Credit':
        CreditModel(amt=get_button.amt,tag=get_button.btn_type).save()
    elif get_button.btn_type == 'Debit':
        DebitModel(amt=get_button.amt,tag=get_button.btn_type).save()
    elif get_button.btn_type == 'Credit Transfer' and get_button.tag == 'Fast Credit Transfer':
        BankTransferModel(amt=get_button.amt,tag=get_button.btn_type).save()
    elif get_button.btn_type == 'Debit Transfer' and get_button.tag == 'Fast Debit Transfer':
        BankTransferModel(amt=get_button.amt,tag=get_button.btn_type).save()
    
    else:pass
    return redirect('/')
    


def ShowChart(request):
    credit_data = CreditModel.objects.all()
    data = []
    lbl = []
    for i in credit_data:
        data.append(i.amt)
        lbl.append(i.add_date)
    
    return JsonResponse({'status':'show'})