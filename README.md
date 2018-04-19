# CKL News

Backend application to manage and serve articles and related data via a RESTful API.

## Contributing

### Running it locally

1. Clone the repository
1. Start a Python virtualenv
1. Install dependencies
1. Create a `local.env` file inside `app/` directory, following `local.env.example` pattern
1. Apply migrations: `python src/manage.py migrate`
1. Create an admin user: `python src/manage.py createsuperuser`
1. Run the development server: `python src/manage.py runserver`
1. Access the Admin Dashboard at: `localhost:8000/admin`
1. Access the API docs at: `localhost:8000/api/docs`

### About tests

1. We use pytest
1. Go to `src/` directory and execute `python -m pytest`
1. When creating new ones, place them inside a `tests.py` file and start each method  with `test_`
1. Use pytest-django fixtures

### Code-style

1. Run `flake8` before pushing changes, we use 100-char-limit per line:  
   (optionally) Install their pre-commit hook with: `python -m flake8 --install-hook git`  
1. Use 4 spaces for indentation.
1. Use `snake_case` for functions and variable names. Use `CamelCase` for class names.
1. For long lists and dictionaries, break lines with one indentation. Use this:  
   ```
   dict = {
       'key': 'value',
       'key2': 'value2',
   }
   ```  
   Instead of:  
   ```
   dict = {'key': 'value',
           'key2: 'value2'}
   ```
1. The same applies for function calls. Use this:  
   ```
   very_very_long_function_name_with_params(
       'param1',
       'param2',
       kw_param1='value',
       kw_param2='value'
   )
   ```  
   Instead of:  
   ```
   very_very_long_function_name_with_params('param1',
                                            'param2',
                                            kw_param1='value',
                                            kw_param2='value')
   ```
1. For classes with multiple-inheritance, do the opposite. Use this:  
   ```
   class VeryLongClassNameWithInheritance(InheritedClass1,
                                          InheritedClass2):
   ```
   Instead of:  
   ```
   class VeryLongClassNameWithInheritance(
       InheritedClass1,
       InheritedClass2
   ):
   ```

### Git workflow

1. We use semantic git messages:
   - Feat: for new functionalities
   - Fix: for bug fixes
   - Docs: updates on documentation only
   - Build: updates on dependencies and build versions
   - Refactor: code changes that neither fix a bug nor add functionality
   - Style: changes on code-style, such as indentation, blank spaces, new lines, camelCase, etc
   - Test: addition of missing tests or fixes on existing tests

1. For new features, start a new branch from `dev` branch, following this convention: `<dev-name>/<feature-name>` (for instance, `bernardo/pagination`)

1. For hotfixes, start a new branch from `master` branch, following this convention `<dev-name>/fix-<fix-name>` (for instance, `bernardo/fix-author-name-typo`)
