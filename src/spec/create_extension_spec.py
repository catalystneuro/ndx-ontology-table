# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec
from hdmf.spec import GroupSpec, NamespaceBuilder


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NamespaceBuilder(
        doc="""Provides a table for linking free-form terms in an NWB file to an ontological terms""",
        name="""ndx-ontology-table""",
        version="""0.1.0""",
        author=list(map(str.strip, """Ben Dichter""".split(','))),
        contact=list(map(str.strip, """ben.dichter@catalystneuro.com""".split(',')))
    )

    ns_builder.include_type('DynamicTable', namespace='hdmf-common')
    #ns_builder.include_type('LabMetaData', namespace='core')


    """
    OntologicalTerms = NWBGroupSpec(
        name='OntologicalTerms',
        doc='Holds ontology metadata',
        neurodata_type_def='OntologicalTerms',
        neurodata_type_inc='LabMetaData',
    )
    """

    OntologyTable = GroupSpec(
        name='OntologyTable',
        data_type_def='OntologyTable',
        data_type_inc='DynamicTable',
        doc='Maps terms in an NWB file to ontological terms'
    )

    OntologyTable.add_dataset(
        name='object_id',
        data_type_inc='VectorData',
        doc='uuid of neurodata_type',
        shape=(None,),
        dtype='text',
        dims=('nterms',)
    )

    OntologyTable.add_dataset(
        name='field_name',
        data_type_inc='VectorData',
        doc='neurodata_type field',
        shape=(None,),
        dtype='text',
        dims=('nterms',)
    )

    OntologyTable.add_dataset(
        name='field_value',
        data_type_inc='VectorData',
        doc='value of field',
        shape=(None,),
        dims=('nterms',)
    )

    OntologyTable.add_dataset(
        name='uri',
        data_type_inc='VectorData',
        doc='uri to match with',
        shape=(None,),
        dtype='text',
        dims=('nterms',)
    )

    """
    OntologyTable.add_group(
        neurodata_type_inc='OntologyLookup',
        quantity=1,
        doc='Maps terms in an NWB file to ontological terms'
    )
    """

    new_data_types = [OntologyTable]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
