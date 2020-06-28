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

    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        if os_name == 'mac' or os_name == 'linux':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        # 'tmpdir'は'pytest'のfixture
        print(tmpdir)
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path)

    def test_csv_file(self, csv_file):
        print(csv_file)
        assert csv_file == 'csv file!!!'
