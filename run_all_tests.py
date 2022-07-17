import unittest
from pathlib import Path
import shutil

print('Starting tests with custom suite.')

tmp_path = Path('./tmp')
if tmp_path.exists():
    shutil.rmtree(tmp_path.absolute())

tmp_path.mkdir()

suite = unittest.TestSuite()
all_test_cases = unittest.defaultTestLoader.discover('.','problem*.py')

for test_case in all_test_cases:
    suite.addTests(test_case)

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

