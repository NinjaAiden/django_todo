# Django To Do

#### A space for learning how to use Django

## Testing

install coverage to see how much of the code is covered by tests using:
- $ sudo pip3 install coverage

run tests only on the project files with:
- $ coverage run --source=todo manage.py test

you can then see a summary of how much is covered with:
- $ coverage report

A detailed report can be generated with:
- $ coverage html

This generates a file called 'htmlcov' with details of what has and has not had tests written for

