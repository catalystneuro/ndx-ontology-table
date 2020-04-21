import os

# Explicitly importing pynwb is required to ensure the global pynwb maps
# are populated.
# noinspection PyUnresolvedReferences
import pynwb  # noqa: F401

from hdmf.common import load_namespaces

# Set path of the namespace.yaml file to the expected install location
ndx_ontology_table_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-ontology-table.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_ontology_table_specpath):
    ndx_ontology_table_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-ontology-table.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_ontology_table_specpath)

from .ontology_table import OntologyTable
