import os

import pytest
import dns_database
import sqlite3 as sl


@pytest.fixture()
def database():
    dns_database.create_database(file_name='test_database.db')
    con = sl.connect('test_database.db')

    yield con

    if os.path.exists('test_database.db'):
        os.remove('test_database.db')


@pytest.fixture()
def domains_list_columns(database):
    sql = 'SELECT * FROM domain_list'
    domain_list = database.execute(sql).description
    columns = [x[0] for x in domain_list]
    return columns


def test_db_domain_list(domains_list_columns):
    assert domains_list_columns == ['id', 'domain', 'client']


@pytest.fixture()
def domains_db_records_columns(database):
    sql = 'SELECT * FROM domain_records'
    domain_records = database.execute(sql).description
    columns = [x[0] for x in domain_records]
    return columns


def test_db_records_columns(domains_db_records_columns):
    assert domains_db_records_columns == ['id', 'domain', 'date', 'NS', 'A', 'MX']


def test_add_domain():
    assert False



