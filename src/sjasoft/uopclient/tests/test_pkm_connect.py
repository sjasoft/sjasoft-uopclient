from sjasoft.uopclient.connect import direct
from sjasoft.uopmeta.schemas.predefined import pkm_schema
from sjasoft.uopdb.sqlite import adaptor
from sjasoft.uopclient.uop_connect import register_adaptor

def test_connect():
    register_adaptor(adaptor.AlchemyDatabase, 'sqlite')
    connect = direct.DirectConnection.connect(db_type='sqlite', db_name='pkm_app',
                                              schemas=[pkm_schema])
    assert connect
