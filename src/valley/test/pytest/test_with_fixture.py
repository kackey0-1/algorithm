import pytest
from pytest import calculation
import os

"""
pytest test_with_fixture.py --cov=calculation
pytest test_with_fixture.py --cov=calculation --cov-report term-missing

テストカバレッジを意識したテストコードを書くこと
Missingがテストされていない行数を示す
----------- coverage: platform linux, python 3.8.3-final-0 -----------
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
calculation.py      14      0   100%
"""


class TestCalTmpdir(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def setup_method(self, method):
        print(f'method={method}')

    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        if os_name == 'mac' or os_name == 'linux':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_value_error(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    def test_save(self, tmpdir):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path)

    def test_save_no_dir(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path)

    def test_csv_file(self, tmpdir, csv_file):
        # 'tmpdir'は'pytest'のfixture
        # 'csv_file'は独自のfixture
        print(tmpdir)
        print(csv_file)
        assert csv_file == 'csv file!!!'
