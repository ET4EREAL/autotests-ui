import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):  # Теперь используем фикстуру
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email="test@mail.ru", username="test_user", password="123456")
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()



