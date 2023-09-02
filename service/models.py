from django.db import models

# Create your models here.


class Data1(models.Model):
    
    school_id=models.IntegerField(max_length=5)
    location_name=models.CharField( max_length=100)
    contact_person_name=models.CharField( max_length=100)
    contact_no=models.CharField( max_length=100)



    site_readiness=models.CharField( max_length=100)
    aipl_dc_no=models.CharField( max_length=100)
    docket_no=models.CharField( max_length=100)
    bill_no=models.CharField( max_length=100)



    computer_desktop=models.CharField(max_length=100)
    interactive_panel=models.CharField( max_length=100)
    invertor=models.CharField( max_length=100)
    io_device=models.CharField( max_length=100)


    
    hd_web_camera=models.CharField(max_length=100)
    ups_for_desktop=models.CharField( max_length=100)
    pa_system=models.CharField( max_length=100)
    multi_printer=models.CharField( max_length=100)

    
    dev_mgmt_app=models.CharField(max_length=100)
    wifi_router=models.CharField( max_length=100)
    
    
