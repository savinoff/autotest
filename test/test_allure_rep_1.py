import allure
import pytest

""" тестовый тест с генерацией allure
"""

def test_success():
    """this test success"""
    assert True

def test_failure():
    assert False

def test_db_conn_1(db_conn_cdb):
    result = db_conn_cdb.execute('select 2 from dual')
    print(result)
    assert result['db_result'] == [1, 2, 3]

@allure.step
def test_db_conn_2(db_conn_cdb):
    result = db_conn_cdb.execute('select 3 from dual')
    print(result)
    assert result['db_result'] == [1, 2, 3]

