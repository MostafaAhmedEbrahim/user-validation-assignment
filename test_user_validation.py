import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from user_validation import UserValidation

class TestUserValidation(unittest.TestCase):

    def test_valid_email_format_returns_true(self):
        email = "mostafa.ahmed@example.com"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_email_missing_at_symbol_returns_false(self):
        email = "mostafaexample.com"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_email_missing_domain_returns_false(self):
        email = "mostafa@"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_email_invalid_tld_returns_false(self):
        email = "mostafa@mail.c"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_email_with_subdomain_returns_true(self):
        email = "mostafa@mail.company.com"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_email_with_special_chars_returns_true(self):
        email = "mostafa.ahmed_21@mail.co"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_uppercase_email_returns_true(self):
        email = "MOSTAFA@MAIL.COM"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_email_with_space_returns_false(self):
        email = "mostafa ahmed@mail.com"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_empty_email_returns_false(self):
        email = ""
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_null_email_returns_false(self):
        email = None
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_valid_username_returns_true(self):
        username = "mostafa_ahmed"
        result = UserValidation.validate_username(username)
        self.assertTrue(result)

    def test_username_too_short_returns_false(self):
        username = "mo"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_too_long_returns_false(self):
        username = "mostafaahmedverylongusername"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_with_spaces_returns_false(self):
        username = "mostafa ahmed"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_with_symbols_returns_false(self):
        username = "mostafa@123"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_with_digits_returns_true(self):
        username = "mostafa123"
        result = UserValidation.validate_username(username)
        self.assertTrue(result)

    def test_empty_username_returns_false(self):
        username = ""
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_null_username_returns_false(self):
        username = None
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_valid_vodafone_number_returns_true(self):
        phone = "01012345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_orange_number_returns_true(self):
        phone = "01234567890"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_etisalat_number_returns_true(self):
        phone = "01198765432"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_we_number_returns_true(self):
        phone = "01555555555"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_vodafone_with_country_code_returns_true(self):
        phone = "201012345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_etisalat_with_country_code_returns_true(self):
        phone = "201112345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_orange_with_country_code_returns_true(self):
        phone = "201212345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_we_with_country_code_returns_true(self):
        phone = "201512345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_invalid_prefix_returns_false(self):
        phone = "01812345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_phone_too_short_returns_false(self):
        phone = "0101234567"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_phone_too_long_returns_false(self):
        phone = "010123456789"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_phone_with_characters_returns_false(self):
        phone = "01012abc678"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_empty_phone_number_returns_false(self):
        phone = ""
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_null_phone_number_returns_false(self):
        phone = None
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_valid_national_id_returns_true(self):
        national_id = "29812251234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertTrue(result)

    def test_national_id_too_short_returns_false(self):
        national_id = "2981225123456"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_national_id_too_long_returns_false(self):
        national_id = "298122512345678"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_national_id_with_letters_returns_false(self):
        national_id = "2981225AB34567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_national_id_invalid_century_code_returns_false(self):
        national_id = "19812251234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_national_id_invalid_month_returns_false(self):
        national_id = "29813251234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_national_id_invalid_day_returns_false(self):
        national_id = "29812323234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_national_id_invalid_governorate_code_returns_false(self):
        national_id = "29812380034567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_empty_national_id_returns_false(self):
        national_id = ""
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_null_national_id_returns_false(self):
        national_id = None
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
