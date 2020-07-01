import os


class Cal(object):
    """
    テストコマンド
    pytest test_with_fixture.py --cov=calculation
    pytest test_with_fixture.py --cov=calculation --cov-report term-missing
    """

    def add_num_and_double(self, x, y):
        print(self)
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

    def save(self, dir_path, file_name):
        print(self)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('tests')