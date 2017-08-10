# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventTypesListResult(Model):
    """Result of the List Event Types operation.

    :param value: A collection of event types
    :type value: list of :class:`EventType
     <azure.mgmt.eventgrid.models.EventType>`
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EventType]'},
    }

    def __init__(self, value=None):
        self.value = value
