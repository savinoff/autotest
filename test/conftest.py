import pytest
from classes.dbconn import DbConnection

# тут хранятся фикстуры для всех тестов (подключения к БД и параметры)

# определим подключение db_conn_cdb
# scope=session для одного соединения со всеми БД для всех тестов и одноразовой инициализации
@pytest.fixture(scope='session')
def db_conn_cdb():
    db_conn_cdb = DbConnection('cdb_user1', 'xxx', 'CDB')
    return db_conn_cdb

