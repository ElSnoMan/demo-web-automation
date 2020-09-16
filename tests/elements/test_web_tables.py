from typing import List
import pytest
from pydantic import BaseModel
from pylenium import Pylenium
from pylenium.element import Element
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def webtable(py):
    return WebTable(py).visit()


def test_add_new_user_to_table(py, webtable):
    py.get('#addNewRecordButton').click()
    py.get('#firstName').type('Carlos')
    py.get('#lastName').type('Kidman')
    py.get('#userEmail').type('test@example.com')
    py.get('#age').type('29')
    py.get('#salary').type('100000')
    py.get('#department').type('The best one')
    py.get('#submit').click()
    assert py.get(".rt-tbody").contains('Carlos')


def test_filter_users_by_email(py, webtable):
    email = 'cierra@example.com'

    py.get('#searchBox').type(email, Keys.ENTER)
    rows = py.find("[role='rowgroup']")

    filtered_rows = webtable.get_filtered_rows_by_email(rows, email)
    assert len(filtered_rows) == 1


def test_emails_in_table_are_unique(py, webtable):
    populated_emails = webtable.get_populated_emails()
    unique_emails = set(populated_emails)
    assert len(unique_emails) == len(populated_emails)


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str


class WebTable:
    def __init__(self, py: Pylenium):
        self.py = py

    table_headers = {
        'First Name': 1,
        'Last Name': 2,
        'Age': 3,
        'Email': 4,
        'Salary': 5,
        'Department': 6
    }

    def visit(self) -> 'WebTable':
        self.py.visit('https://demoqa.com/webtables')
        return self

    def get_column_cells_by_name(self, column_name) -> List[Element]:
        header = self.table_headers[column_name]
        return self.py.findx(f"//div[@role='rowgroup']/div//div[{header}]")

    def get_populated_emails(self) -> List[str]:
        """ Gets a list of all populated emails as strings. """
        email_cells = self.get_column_cells_by_name('Email')
        return [cell.text() for cell in email_cells if cell.text() != ' ']

    def get_filtered_rows_by_email(self, rows, email) -> List[Element]:
        return [row for row in rows if email in row.text()]

    def get_user_by_email(self, email) -> User:
        users = self.get_all_users()
        return next(user for user in users if user.email == email)

    def get_all_users(self) -> List[User]:
        users = list()
        rows = self.py.find("[role='rowgroup']")

        for row in rows:
            cells = row.find('.rt-td')
            users.append(User(
                first_name=cells[0].text(),
                last_name=cells[1].text(),
                age=int(cells[2].text()),
                salary=int(cells[3].text()),
                department=cells[4].text()))
        return users
