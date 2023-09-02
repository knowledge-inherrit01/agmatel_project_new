from django.http import HttpResponse
from django.shortcuts import render
from service.resources import DataResource
from service.models import Data1
from tablib import Dataset




def homePage(request):

    	return render (request,"index.html"); 


def adminPage(request):

    	return render (request,"admin.html"); 





def loginPage(request):
    
       
    msg=""

    
    if request.method=='POST':
    
      
        id=request.POST['userid']
        passw=request.POST['password']

        


        if id=='admin' and passw=='Asdf@12345':
                
                return render(request,"dataUpload.html")
        
        else:
                msg="Login Failed !"
                return render(request,"admin.html",{'msg':msg})
        


def upload(request):
        msg=''
       

        if request.method== 'POST':
          data_resource=DataResource()
          dataset=Dataset()
          newData=request.FILES['upload']
          importData=dataset.load(newData.read(),format='xlsx')

          for data in importData:
                value=Data1(
                      
                      data[0],
                      data[1],
                      data[2],
                      data[3],
                      data[4],
                      data[5],
                      data[6],
                      data[7],
                      data[8],
                      data[9],
                      data[10],
                      data[11],
                      data[12],
                      data[13],
                      data[14],
                      data[15],
                      data[16],
                      data[17],
                      data[18],
                     
                    
                )
                value.save()
                msg='Data Upload Success !!!'

        return render(request,"dataUpload.html",{"msg":msg})



   
      


       



def formPage(request):
    msg='none'

    id=request.POST['id']

    try:

        data=Data1.objects.get(school_id=id)
        msg='success'
        print(data)

        context={
                'mydata':data
        }
        return render (request,"Form.html",context)
    
    except Exception:
          msg="Data not found "

          return render (request,"Form.html",{'message':msg})

          


    
 




