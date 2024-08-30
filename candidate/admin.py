from django.contrib import admin
from . import models
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['title','company_name','description','requirements','location','created_at'] # nicher function
    # er name gula use korte hobe ekhane.
    
    def first_name(self,obj): # name gula nijer moto kore dite parbe
        return obj.user.first_name # Candidate er sathe user model er connection ache tai user model er kache giye tar first name ke ber kore anlam
    
    def last_name(self,obj):
        return obj.user.last_name
    
    
admin.site.register(models.Candidate, CandidateAdmin)