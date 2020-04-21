from hdmf.common import DynamicTable, register_class, register_map
from hdmf.common.io.table import DynamicTableMap
from hdmf.utils import docval, call_docval_func, get_docval


@register_class('OntologyTable', 'ndx-ontology-table')
class OntologyTable(DynamicTable):
    """Maps terms in an NWB file to ontological terms"""

    __columns__ = (
        {'name': 'object_id', 'description': 'uuid of neurodata_type', 'required': True},
        {'name': 'field_name', 'description': 'neurodata_type field', 'required': True},
        {'name': 'field_value', 'description': 'value of field', 'required': True},
        {'name': 'uri', 'description': 'uri that matches this term', 'required': True}
    )

    @docval(dict(name='description', type=str, doc='You may add a custom description',
                 default="Maps terms in an NWB file to ontological terms"),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        kwargs['name'] = 'OntologyTable'
        call_docval_func(super(OntologyTable, self).__init__, kwargs)


@register_map(OntologyTable)
class OntologyTableMap(DynamicTableMap):
    pass
