import sqlite3 as sl


def create_database(file_name='dns_database.db'):
    con = sl.connect(file_name)
    sql = '''
    CREATE TABLE IF NOT EXISTS domain_list (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    domain TEXT,
    client TEXT)'''
    con.execute(sql)
    con.commit()

    sql = '''
    CREATE TABLE IF NOT EXISTS domain_records (
    id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    domain TEXT, 
    date DATETIME,
    NS TEXT, 
    A TEXT, 
    MX TEXT, 
    FOREIGN KEY(domain) REFERENCES domain_list(domain))'''
    con.execute(sql)
    con.commit()


def add_domain():
    pass