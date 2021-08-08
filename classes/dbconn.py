from collections import namedtuple
from time import sleep


class DbConnection():
    """Класс - пример для взаимодействия с БД"""
    def __init__(self, user: str, password: str, tns: str):
        print(f'db object creating user={user}, password={password}, tns={tns}')
        self.connected = False
        self.user = user
        self.password = password
        self.tns = tns

    def _connect(self):
        print('connecting...')
        sleep(.5)
        self.connected = True
        print('connected ok')

    def execute(self, exec_str):
        """Выполнить запрос, возвращает строку запроса и результат"""
        print(f'execution on {self.user}@{self.tns}, exec_string="{exec_str}"')
        if not self.connected:
            self._connect()
        DbResult = namedtuple('DbResult', ['exec_string', 'db_result'])
        result = DbResult(exec_str, [1, 2, 3])
        print('exec ok')
        result_dict = result._asdict()
        return result._asdict()


if __name__ == '__main__':
    dbc1 = DbConnection('test_user', 'test_pass', 'TNS1')
    res = dbc1.execute('select 1 from dual')
    print(res)
