from django.contrib import admin
from taller.models import Asesor, Operation, PreCita, Cita
from niv.models import Niv

import pdb

# 3rd party
from import_export import resources
from import_export.fields import Field
from import_export import fields
from import_export.admin import ImportExportMixin, ExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget 
from import_export import widgets


#Modified (ForeignKeys) for create the objects that DoesNotExist
class TallerCreateWidget(ForeignKeyWidget):
	def clean(self, value, row=None, *args, **kwargs):
		#pdb.set_trace()
		return self.model.objects.get(niv = value)[0]


#************Below this line are the Resources for the models***********

#For Operation
class OperationResource(resources.ModelResource):

	niv = Field(
		attribute='niv',
		column_name = 'niv',
		widget=ForeignKeyWidget(Niv, 'niv')
		)

	class Meta:
		
		model = Operation
		
		exclude = ('id',)
		import_id_fields = ['niv','job','date','description']


class OperationResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = OperationResource
	list_display = ('niv', 'job', 'date', 'description')



#For PreCita
class PreCitaResource(resources.ModelResource):

	class Meta:
		model = PreCita


class PreCitaResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = PreCitaResource
	list_display = ('niv', 'preferred_date')


#For Citas
class CitaResource(resources.ModelResource):

	class Meta:
		model = Cita


class CitaResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = CitaResource
	list_display = ('niv', 'adviser', 'seen')


admin.site.register(Asesor)
admin.site.register(Operation, OperationResAdmin)
admin.site.register(PreCita, PreCitaResAdmin)
admin.site.register(Cita, CitaResAdmin)