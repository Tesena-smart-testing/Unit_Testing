#Installation Coverage
pip install coverage

#Run tests
pytest
coverage run -m unittest discover

#Run Specific tests
pytest -k test_add_positive_numbers
coverage run -m unittest test_even_odd.TestCheckNumber.test_positive_even

coverage run test_even_odd.py

#Report in Console
coverage report
pytest --junit-xml=report.xml test_my_method

#Report in HTML
coverage html
pytest --html=report.html test_my_method
