# coding: utf-8

from wtforms import fields as _fields
from wtforms import widgets as _widgets
from wtforms.validators import ValidationError
from flask_wtf import FlaskForm
from flask_admin.babel import Translations
from quokka.admin.wtforms_html5 import AutoAttrMeta
from quokka.admin.fields import SmartSelect2Field
from flask_admin.form.fields import (
    DateTimeField,
    TimeField,
    Select2Field,
    Select2TagsField,
    JSONField
)
from flask_admin.form.widgets import Select2TagsWidget
from flask_admin.model.fields import (
    InlineFieldList,
    InlineFormField
)
from flask_admin.form import rules  # noqa
from wtforms import validators  # noqa
# from wtforms_components import read_only  # noqa
# from wtforms_components import ReadOnlyWidgetProxy  # noqa


class PassiveField(object):
    """
    Passive field that does not populate obj values.
    """
    def populate_obj(self, obj, name):
        pass


class PassiveHiddenField(PassiveField, _fields.HiddenField):
    pass


class PassiveStringField(PassiveField, _fields.StringField):
    pass


fields = _fields  # noqa
fields.SmartSelect2Field = SmartSelect2Field
fields.DateTimeField = DateTimeField
fields.TimeField = TimeField
fields.Select2Field = Select2Field
fields.Select2TagsField = Select2TagsField
fields.JSONField = JSONField
fields.InlineFieldList = InlineFieldList
fields.InlineFormField = InlineFormField
fields.PassiveHiddenField = PassiveHiddenField
fields.PassiveStringField = PassiveStringField

widgets = _widgets
widgets.Select2TagsWidget = Select2TagsWidget


READ_ONLY = {'readonly': True}


class Form(FlaskForm):
    """Base class to customize wtforms"""
    _translations = Translations()
    Meta = AutoAttrMeta

    def _get_translations(self):
        return self._translations


class CallableValidator(object):
    """
    Takes a callable and validates using it
    """
    def __init__(self, function, message=None):
        self.function = function
        self.message = message

    def __call__(self, form, field):
        validation = self.function(form, field)
        if validation is not None:
            raise ValidationError(self.message or validation)


validators.CallableValidator = CallableValidator
