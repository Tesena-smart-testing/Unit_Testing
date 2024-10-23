#Installation Coverage
pip install coverage

#Run tests
coverage run -m unittest discover

#Run Specific tests
coverage run -m unittest test_even_odd.TestCheckNumber.test_positive_even

coverage run test_even_odd.py

#Report in Console
coverage report

#Report in HTML
coverage html
