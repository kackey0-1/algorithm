import pytest
import calculation
import os

class TestCalTmpdir(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'

    def setup_method(self, method):
        print(f'method={method}')

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir, csv_file):
        # 'tmpdir'は'pytest'のfixture
        self.cal.save(tmpdir, self.test_file_name)
        # csv_fileは'conftest'のfixture
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path)
