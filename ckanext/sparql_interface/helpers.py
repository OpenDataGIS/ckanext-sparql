from urllib.parse import urlparse
import ckan.plugins as p
from ckanext.sparql_interface.utils import sparqlQuery as utils_sparqlQuery
from logging import getLogger


logger = getLogger(__name__)

all_helpers = {}

def helper(fn):
    """
    collect helper functions into ckanext.sparql.all_helpers dict
    """
    all_helpers[fn.__name__] = fn
    return fn

### GET FUNCTIONS ###

#Returns get/post query param data

@helper
def get_query():
    return p.toolkit.request.params.get('query')

#Returns get/post direct_link param to check whether to return in a specific format the data

@helper
def check_direct_link():
    return p.toolkit.request.params.get('direct_link')

#Used to check whether a string is a url

@helper
def check_is_url(strtocheck):
    results = urlparse(strtocheck)
    return results.scheme

@helper
def sparql_endpoint_url():
    endpointUrl = p.toolkit.config.get('ckanext.sparql_interface.endpoint_url', 'http://dbpedia.org/sparql')
    #logger.debug("endpointUrl: " + endpointUrl)
    return endpointUrl

@helper
def sparql_hide_endpoint_url():
    hideEndpointUrl = p.toolkit.asbool(p.toolkit.config.get('ckanext.sparql_interface.hide_endpoint_url', 'False'))
    #logger.debug("hideEndpointUrl: %s" % hideEndpointUrl)
    return hideEndpointUrl

@helper
def sparql_query_prefixes():
    queryPrefixes = p.toolkit.config.get('ckanext.sparql_interface.query_prefixes', 'PREFIX void: <http://rdfs.org/ns/void#> PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX vann: <http://purl.org/vocab/vann/> PREFIX teach: <http://linkedscience.org/teach/ns#> PREFIX dcterms: <http://purl.org/dc/terms/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX dcat: <http://www.w3.org/ns/dcat#> PREFIX crsw: <http://courseware.rkbexplorer.com/ontologies/courseware#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX aiiso: <http://purl.org/vocab/aiiso/schema#> PREFIX univcat: <http://data.upf.edu/upf/ontologies/universidadcatalana#> PREFIX skos: <http://www.w3.org/2004/02/skos/core#> PREFIX vivo: <http://vivoweb.org/ontology/core#> PREFIX sbench: <http://swat.cse.lehigh.edu/onto/univ-bench.owl#> PREFIX sdmx-attribute: <http://purl.org/linked-data/sdmx/2009/attribute#> PREFIX sdmx-concept: <http://purl.org/linked-data/sdmx/2009/concept#> PREFIX sdmx-code: <http://purl.org/linked-data/sdmx/2009/code#> PREFIX disco: <http://rdf-vocabulary.ddialliance.org/discovery#> PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> PREFIX sdmx-measure: <http://purl.org/linked-data/sdmx/2009/measure#> PREFIX qb: <http://purl.org/linked-data/cube#> PREFIX sdmx: <http://purl.org/linked-data/sdmx#>')
    #logger.debug("queryPrefixes: " + queryPrefixes)
    return queryPrefixes

@helper
def sparqlQuery(data_structure):
    return utils_sparqlQuery(data_structure)