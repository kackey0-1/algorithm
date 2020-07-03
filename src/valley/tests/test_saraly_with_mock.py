"""
mock
ネットワーク越しにデータ処理をする場合、
処理を擬似的に実装し、テストをする方法
"""

import unittest
from unittest.mock import MagicMock
from unittest import mock
import salary


class TestSalary(unittest.TestCase):
    # def setUp(self):
    #     self.patcher = mock.patch('salary.ThirdPartyBonusRestApi')
    #     self.mock_bonus = self.patcher.start()

    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        # 呼び出しの検証
        s.bonus_api.bonus_price.assert_called()
        # 呼び出し回数の検証
        s.bonus_api.bonus_price.assert_called_once()
        # 引数の検証
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        # 呼び出し回数の検証 & 引数の検証
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        # 呼び出し回数の検証
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        # 呼び出しの検証
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    def test_calculation_salary_patch(self, mock_bonus):
        # mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    def test_calculation_salary_patch(self):
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()
