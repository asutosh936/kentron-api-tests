# kentron-api-tests
kentron-api-tests is responsible to document all the automated functional test cases for backend apis using Pytest framework


### Step 1: 
#### Set Up Your Python Environment
* Install Python: Ensure Python 3.x is installed on your system. 
* Verify with:
```python
python3 --version
```

#### Create a Virtual Environment: Set up an isolated Python environment for your project:

```python
python3 -m venv myapi-env
cd myapi-env
source bin/activate  # On Windows: myapi-env\Scripts\activate

```
#### Install Required Libraries:
```python
pip install pytest requests pytest-html
```

### Step 2: Create a Basic Flask Application

#### Set Up the Project Directory: Create a directory structure for your project:
```python
project/
│
├── tests/
│   ├── test_api.py
│   ├── conftest.py
│   ├── auth_helpers.py
│
├── requirements.txt
├── pytest.ini

```

### Step 3: Run Tests and Generate Report

#### Run the tests and generate the HTML report:
```python
pytest tests/

```
#### After execution, the report will be available at `reports/kentron_test_report.html`.
