from django.shortcuts import render, redirect
from django.contrib import messages
import hashlib
from onepassword.forms import OnePasswordForm

def main(request):
    form  = OnePasswordForm()

    if request.method == "POST":
        form = OnePasswordForm(request.POST)
        
        if form.is_valid():
            onepassword = hashlib.sha256(form.cleaned_data.get("onepassword").encode())
            
            
            onepassword = onepassword.hexdigest() + form.cleaned_data.get("keyword")
            
            encryptedPassword = hashlib.sha256(onepassword.encode()).hexdigest()[:16]
            
            messages.warning(request,"Password Will Disappearing within 15 seconds")
            form  = OnePasswordForm()

            return render(
                request,'navbar/password.html',
                {'form':form,'encryptedPassword':encryptedPassword}
            )
        
        
        messages.error(request,"Error occured")
        return render(request,'navbar/password.html',{'form':form})
    
    
    return render(
        request,'navbar/password.html',
        {'form':form}
    )


def howitworks(request):
    return render(request,'navbar/howitworks.html')

def page_not_found(request,exception):
    return render(request,"error/404.html")


def internal_error(request):
    return render(request,"error/500.html")