# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TopicTypesListResult(Model):
    """Result of the List Topic Types operation.

    :param value: A collection of topic types
    :type value: list of :class:`TopicTypeInfo
     <azure.mgmt.eventgrid.models.TopicTypeInfo>`
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TopicTypeInfo]'},
    }

    def __init__(self, value=None):
        self.value = value
