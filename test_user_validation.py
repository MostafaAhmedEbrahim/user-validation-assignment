import unittest
import sys
import os

# Add the current directory to Python path to import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from user_validation import UserValidation


class TestUserValidation(unittest.TestCase):

    # === Email Validation Tests ===

    def test_valid_email_format_returns_true(self):
        """Test that valid email format returns True"""
        # Arrange
        email = "user@example.com"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertTrue(result)

    def test_email_missing_at_symbol_returns_false(self):
        """Test that email missing @ symbol returns False"""
        # Arrange
        email = "userexample.com"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertFalse(result)

    def test_email_missing_domain_returns_false(self):
        """Test that email missing domain returns False"""
        # Arrange
        email = "user@"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertFalse(result)

    def test_email_invalid_tld_returns_false(self):
        """Test that email with invalid TLD returns False"""
        # Arrange
        email = "user@mail.c"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertFalse(result)

    def test_email_with_subdomain_returns_true(self):
        """Test that email with subdomain returns True"""
        # Arrange
        email = "user@mail.company.com"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertTrue(result)

    def test_email_with_special_chars_returns_true(self):
        """Test that email with valid special characters returns True"""
        # Arrange
        email = "ramy.gomaa_21@mail.co"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertTrue(result)

    def test_uppercase_email_returns_true(self):
        """Test that uppercase email returns True"""
        # Arrange
        email = "USER@MAIL.COM"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertTrue(result)

    def test_email_with_space_returns_false(self):
        """Test that email with space returns False"""
        # Arrange
        email = "user name@mail.com"

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertFalse(result)

    def test_empty_email_returns_false(self):
        """Test that empty email returns False"""
        # Arrange
        email = ""

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertFalse(result)

    def test_null_email_returns_false(self):
        """Test that None email returns False"""
        # Arrange
        email = None

        # Act
        result = UserValidation.validate_email(email)

        # Assert
        self.assertFalse(result)

    # === Username Validation Tests ===

    def test_valid_username_returns_true(self):
        """Test that valid username returns True"""
        # Arrange
        username = "ramy_gomaa"

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertTrue(result)

    def test_username_too_short_returns_false(self):
        """Test that username too short returns False"""
        # Arrange
        username = "ab"

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertFalse(result)

    def test_username_too_long_returns_false(self):
        """Test that username too long returns False"""
        # Arrange
        username = "ramygomaalsaverylongusername"

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertFalse(result)

    def test_username_with_spaces_returns_false(self):
        """Test that username with spaces returns False"""
        # Arrange
        username = "ramy gomaa"

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertFalse(result)

    def test_username_with_symbols_returns_false(self):
        """Test that username with symbols returns False"""
        # Arrange
        username = "ramy@123"

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertFalse(result)

    def test_username_with_digits_returns_true(self):
        """Test that username with digits returns True"""
        # Arrange
        username = "ramy123"

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertTrue(result)

    def test_empty_username_returns_false(self):
        """Test that empty username returns False"""
        # Arrange
        username = ""

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertFalse(result)

    def test_null_username_returns_false(self):
        """Test that None username returns False"""
        # Arrange
        username = None

        # Act
        result = UserValidation.validate_username(username)

        # Assert
        self.assertFalse(result)

    # === Phone Number Validation Tests ===

    def test_valid_vodafone_number_returns_true(self):
        """Test that valid Vodafone number returns True"""
        # Arrange
        phone = "01012345678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_orange_number_returns_true(self):
        """Test that valid Orange number returns True"""
        # Arrange
        phone = "01234567890"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_etisalat_number_returns_true(self):
        """Test that valid Etisalat number returns True"""
        # Arrange
        phone = "01198765432"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_we_number_returns_true(self):
        """Test that valid WE number returns True"""
        # Arrange
        phone = "01555555555"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_vodafone_with_country_code_returns_true(self):
        """Test that valid Vodafone with country code returns True"""
        # Arrange
        phone = "201012345678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_etisalat_with_country_code_returns_true(self):
        """Test that valid Etisalat with country code returns True"""
        # Arrange
        phone = "201112345678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_orange_with_country_code_returns_true(self):
        """Test that valid Orange with country code returns True"""
        # Arrange
        phone = "201212345678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_valid_we_with_country_code_returns_true(self):
        """Test that valid WE with country code returns True"""
        # Arrange
        phone = "201512345678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertTrue(result)

    def test_invalid_prefix_returns_false(self):
        """Test that invalid prefix returns False"""
        # Arrange
        phone = "01812345678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertFalse(result)

    def test_phone_too_short_returns_false(self):
        """Test that phone too short returns False"""
        # Arrange
        phone = "0101234567"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertFalse(result)

    def test_phone_too_long_returns_false(self):
        """Test that phone too long returns False"""
        # Arrange
        phone = "010123456789"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertFalse(result)

    def test_phone_with_characters_returns_false(self):
        """Test that phone with characters returns False"""
        # Arrange
        phone = "01012abc678"

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertFalse(result)

    def test_empty_phone_number_returns_false(self):
        """Test that empty phone number returns False"""
        # Arrange
        phone = ""

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertFalse(result)

    def test_null_phone_number_returns_false(self):
        """Test that None phone number returns False"""
        # Arrange
        phone = None

        # Act
        result = UserValidation.validate_phone_number(phone)

        # Assert
        self.assertFalse(result)

    # === National ID Validation Tests ===

    def test_valid_national_id_returns_true(self):
        """Test that valid national ID returns True"""
        # Arrange
        national_id = "29812251234567"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertTrue(result)

    def test_national_id_too_short_returns_false(self):
        """Test that national ID too short returns False"""
        # Arrange
        national_id = "2981225123456"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_national_id_too_long_returns_false(self):
        """Test that national ID too long returns False"""
        # Arrange
        national_id = "298122512345678"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_national_id_with_letters_returns_false(self):
        """Test that national ID with letters returns False"""
        # Arrange
        national_id = "2981225AB34567"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_century_code_returns_false(self):
        """Test that invalid century code returns False"""
        # Arrange
        national_id = "19812251234567"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_month_returns_false(self):
        """Test that invalid month returns False"""
        # Arrange
        national_id = "29813251234567"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_day_returns_false(self):
        """Test that invalid day returns False"""
        # Arrange
        national_id = "29812323234567"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_national_id_invalid_governorate_code_returns_false(self):
        """Test that invalid governorate code returns False"""
        # Arrange
        national_id = "29812380034567"

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_empty_national_id_returns_false(self):
        """Test that empty national ID returns False"""
        # Arrange
        national_id = ""

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)

    def test_null_national_id_returns_false(self):
        """Test that None national ID returns False"""
        # Arrange
        national_id = None

        # Act
        result = UserValidation.validate_national_id(national_id)

        # Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()