from django.contrib import admin

from niv.models import Niv, VehicleModel

import pdb

# 3rd party 
from import_export import resources
from import_export.fields import Field
from import_export import fields
from import_export.admin import ImportExportMixin, ExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget 
from import_export import widgets
# Register your models here.

#Modified (ForeignKeys) for create the objects that DoesNotExist
class VehicleModelCreateWidget(ForeignKeyWidget):
	def clean(self, value, row=None, *args, **kwargs):
		#pdb.set_trace()
		return self.model.objects.get_or_create(model = value)[0]


#************Below this line are the Resources for the models***********


#For VehiclesModels
class VehicleModelResource(resources.ModelResource):

	class Meta:
		model = VehicleModel


class VehicleModelResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = VehicleModelResource
	list_display = ('model', 'description')



#For NIV
class NivResource(resources.ModelResource):

	model = Field(
		attribute='model',
		column_name = 'model',
		widget=VehicleModelCreateWidget(VehicleModel, 'model')
		)

	class Meta:
		model = Niv
		exclude = ('id',)
		import_id_fields = ['model','niv','owner','address','city',
			'telephone','phone','fax','client_id','email','birthdate',
			'purchase_date','invoice_number','niv_assignment','job_queue','vin',
			'motor_number','brand','color','year','plate_number','reference','sold_by',
			'identification','last_job','zone']


class NivResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = NivResource
	list_display = ('niv', 'owner')


admin.site.register(VehicleModel, VehicleModelResAdmin)
admin.site.register(Niv, NivResAdmin)
