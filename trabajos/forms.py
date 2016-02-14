# -*- coding: utf-8 -*-
from trabajos.models import Trabajo
from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin, NgModelForm
from crispy_forms.helper import FormHelper


class TrabajoForm(NgModelFormMixin, forms.ModelForm):
    """
    Job Form with a little crispy forms added!
    """
    def __init__(self, *args, **kwargs):
        super(TrabajoForm, self).__init__(*args, **kwargs)
        setup_bootstrap_helpers(self)

    class Meta:
        model = Trabajo
        fields = ('nombre', 'descripcion',)


def setup_bootstrap_helpers(object):
    object.helper = FormHelper()
    object.helper.form_class = 'form-horizontal'
    object.helper.label_class = 'col-lg-3'
    object.helper.field_class = 'col-lg-8'
