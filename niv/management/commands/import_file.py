# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mimetypes
import argparse

from django.utils.encoding import force_text
from django.utils.translation import ugettext as _
from django.core.management.base import BaseCommand
from django.db import transaction

from import_export.formats import base_formats

from django.apps import apps as django_apps

#for testing
import pdb


FORMATS = {
    'text/csv': base_formats.CSV,
    'application/vnd.ms-excel': base_formats.XLS,
    'application/json': base_formats.JSON,
}


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter

        # Positional arguments
        parser.add_argument('file_path',
            metavar='file_path',
            nargs=1,
            help='File path to import.')
        parser.add_argument('-r','--resource-class',
                    dest='resource_class',
                    default=None,
                    help='Resource class as dotted path, ie: mymodule.resources.MyResource')  # noqa
        parser.add_argument('-m', '--model-name',
                    dest='model_name',
                    default=None,
                    help='Model name, ie: auth.User')  # noqa
        parser.add_argument('-n', '--dry-run',
                    action='store_true',
                    dest='dry_run',
                    default=False,
                    help='Dry run')
        parser.add_argument('-e', '--raise-errors',
                    action='store_true',
                    dest='raise_errors',
                    help='Raise errors')
        parser.add_argument('-q', '--no-raise-errors',
                    action='store_false',
                    dest='raise_errors',
                    help='Do not raise errors')

    def get_resource_class(self, resource_class, model_name):
        from django.utils.module_loading import import_string
        from import_export.resources import modelresource_factory

        if not resource_class:
            return modelresource_factory(django_apps.get_model(model_name))
        else:
            return import_string(resource_class)

    @transaction.atomic
    def handle(self, **options):
        dry_run = options.get('dry_run')
        if dry_run:
            self.stdout.write(self.style.NOTICE(_('Dry run')))
        raise_errors = options.get('raise_errors', None)
        if raise_errors is None:
            raise_errors = not dry_run        
        
        import_file_name = options['file_path'][0]
        mimetype, encoding = mimetypes.guess_type(import_file_name)
        input_format = FORMATS[mimetype]()
        resource_class = self.get_resource_class(
            options.get('resource_class'),
            options.get('model_name')
        )
        resource = resource_class()
        
        import_file = open(import_file_name, input_format.get_read_mode())
        data = import_file.read()
        dataset = input_format.create_dataset(data)
        #pdb.set_trace()
        result = resource.import_data(
            dataset,
            dry_run=dry_run,
            raise_errors=raise_errors
        )
        
        if result.has_errors():
            self.stdout.write(self.style.ERROR(_('Errors')))
            for error in result.base_errors:
                self.stdout.write(error.error, self.style.ERROR)
            for line, errors in result.row_errors():
                for error in errors:
                    self.stdout.write(self.style.ERROR(
                        _('Line number') + ': ' + force_text(line) + ' - '
                        + force_text(error.error)))
        else:
            self.stdout.write(self.style.NOTICE(_('OK')))
            import_file.close()