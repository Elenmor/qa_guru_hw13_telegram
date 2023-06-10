import time
from selene import have, command
from tests import resource


class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone = browser.element('#userNumber')
        self.state = browser.element('#state')
        self.subject = browser.element('#subjectsInput')
        self.adress = browser.element('#currentAddress')
        self.city = browser.element('#city')

    def open(self):
        self.browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_gender(self, gender):
        self.browser.element(f'[value={gender}] + label').click()
        return self

    def fill_phone(self, value):
        self.phone.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, value):
        self.subject.type(value).press_enter()
        return self

    def fill_hobby(self, value):
        self.browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_file(self, file_name):
        self.browser.element('#uploadPicture').send_keys(resource.path(file_name))
        time.sleep(1)
        return self

    def fill_adress(self, value):
        self.adress.type(value)
        return self

    def fill_city(self, name):
        self.city.click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_state(self, name):
        #self.browser.element("footer").execute_script('element.remove()')
        self.browser.execute_script('document.querySelector("#fixedban").remove()')
        self.browser.element('footer').execute_script('element.remove()')
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def click_submit(self):
        # self.browser.element('#submit').perform(command.js.click)
        self.browser.element('[id="submit"]').perform(command.js.scroll_into_view)
        self.browser.element('[id="submit"]').press_enter()

    def should_registered_user_with(self, *args):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(args)
        )
        return self

    def assert_user_data(self, *args):
        self.browser.all('tbody tr').should(have.exact_texts(*args))
        return self

    # def should_registered_user_with(self, *args):

    # self.browser.element('.table').all('td').even.should(
    #   have.exact_texts(args)
    # )
    # return self
