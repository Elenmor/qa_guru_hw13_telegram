import allure
from models.registration_page import RegistrationPage


@allure.title("Successful fill form")
def test_successful(setup_browser):
    registration_page = RegistrationPage(setup_browser)

    with allure.step("open_browser"):
        registration_page.open()

    with allure.step("Fill form"):
        registration_page.fill_first_name('Helen').fill_last_name('Morilova')
        registration_page.fill_email('test@test.ru')
        registration_page.fill_gender('Female')
        registration_page.fill_phone('1234567890')

    with allure.step("fill_date_of_birth"):
        registration_page.fill_date_of_birth('1984', 'May', '12')

    with allure.step("Fill subject and hobby"):
        registration_page.fill_subject('Arts')
        registration_page.fill_hobby('Sports')

    with allure.step("Upload_file"):
        registration_page.upload_file('404-img.png')

    with allure.step("fill_adress"):
        registration_page.fill_adress('adress street, 1')
        registration_page.fill_state('NCR')
        registration_page.fill_city('Delhi')

    with allure.step("Subit"):
        registration_page.click_submit()

    with allure.step("Check form results"):
        registration_page.should_registered_user_with(
            'Helen Morilova',
            'test@test.ru',
            'Female',
            '1234567890',
            '12 May,1984',
            'Arts',
            'Sports',
            '404-img.png',
            'adress street, 1',
            'NCR Delhi',
        )
