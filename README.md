# CKL News

Backend application to manage and serve articles and related data via a RESTful API.

## Contributing

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
