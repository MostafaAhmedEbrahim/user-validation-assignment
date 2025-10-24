import re


class UserValidation:

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates if the provided email is in a proper format."""
        if email is None:
            return False

        if not isinstance(email, str) or email.strip() == "":
            return False

        # Regular expression for email validation
        pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if email matches pattern and doesn't contain spaces
        if re.match(pattern, email) and ' ' not in email:
            return True

        return False

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validates username (3-20 chars, letters/numbers/underscore only)."""
        if username is None:
            return False

        if not isinstance(username, str):
            return False

        # Check length
        if len(username) < 3 or len(username) > 20:
            return False

        # Check if contains only allowed characters (letters, numbers, underscore)
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False

        return True

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """Validates Egyptian phone number (starts with 010, 011, 012, 015 or 20 10,20 11,20 12,20 15 - 11 digits total or 12 if it starts with 2)."""
        if phone is None:
            return False

        if not isinstance(phone, str):
            return False

        # Remove any spaces or dashes that might be present
        phone = phone.replace(' ', '').replace('-', '')

        # Check if contains only digits
        if not phone.isdigit():
            return False

        # Check for local format (11 digits starting with 010, 011, 012, 015)
        if len(phone) == 11:
            valid_prefixes = ['010', '011', '012', '015']
            return phone[:3] in valid_prefixes

        # Check for international format (12 digits starting with 20)
        elif len(phone) == 12:
            if phone.startswith('20'):
                # Get the operator code (first two digits after country code)
                operator_code = phone[2:4]
                valid_operator_codes = ['10', '11', '12', '15']
                return operator_code in valid_operator_codes

        return False

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """Validates Egyptian national ID (14 digits with valid date and governorate code)."""
        if national_id is None:
            return False

        if not isinstance(national_id, str):
            return False

        # Check if it's exactly 14 digits
        if len(national_id) != 14 or not national_id.isdigit():
            return False

        # Extract components
        century_code = national_id[0]
        year = national_id[1:3]
        month = national_id[3:5]
        day = national_id[5:7]
        governorate_code = national_id[7:9]

        # Validate century code (2 for 1900s, 3 for 2000s)
        if century_code not in ['2', '3']:
            return False

        # Validate month (01-12)
        if not (1 <= int(month) <= 12):
            return False

        # Validate day (01-31)
        if not (1 <= int(day) <= 31):
            return False

        # Additional date validation for specific months
        month_int = int(month)
        day_int = int(day)

        # April, June, September, November have 30 days
        if month_int in [4, 6, 9, 11] and day_int > 30:
            return False

        # February validation
        if month_int == 2:
            # Simple check - February has max 29 days
            if day_int > 29:
                return False

        # Validate governorate code (01-88)
        governorate_num = int(governorate_code)
        if not (1 <= governorate_num <= 88):
            return False

        return True


# Test code to verify all functions
if __name__ == "__main__":
    print("=== Testing UserValidation Class ===")

    # Test email validation
    print("\n📧 Email Validation Tests:")
    email_cases = [
        ("user@example.com", True),
        ("userexample.com", False),
        ("user@", False),
        ("user@mail.c", False),
        ("user@mail.company.com", True),
        ("ramy.gomaa_21@mail.co", True),
        ("USER@MAIL.COM", True),
        ("user name@mail.com", False),
        ("", False),
        (None, False)
    ]

    for email, expected in email_cases:
        result = UserValidation.validate_email(email)
        status = "✅" if result == expected else "❌"
        print(f"{status} {email} -> {result} (expected: {expected})")

    # Test phone number validation
    print("\n📱 Phone Number Validation Tests:")
    phone_cases = [
        ("01012345678", True),  # Vodafone
        ("01234567890", True),  # Orange
        ("01198765432", True),  # Etisalat
        ("01555555555", True),  # WE
        ("201012345678", True),  # Vodafone with country code
        ("201112345678", True),  # Etisalat with country code
        ("201212345678", True),  # Orange with country code
        ("201512345678", True),  # WE with country code
        ("01812345678", False),  # Invalid prefix
        ("0101234567", False),  # Too short
        ("010123456789", False),  # Too long
        ("01012abc678", False),  # Contains characters
        ("", False),  # Empty
        (None, False)  # None
    ]

    for phone, expected in phone_cases:
        result = UserValidation.validate_phone_number(phone)
        status = "✅" if result == expected else "❌"
        print(f"{status} {phone} -> {result} (expected: {expected})")

    # Test username validation
    print("\n👤 Username Validation Tests:")
    username_cases = [
        ("ramy_gomaa", True),
        ("ab", False),
        ("ramygomaalsaverylongusername", False),
        ("ramy gomaa", False),
        ("ramy@123", False),
        ("ramy123", True),
        ("", False),
        (None, False)
    ]

    for username, expected in username_cases:
        result = UserValidation.validate_username(username)
        status = "✅" if result == expected else "❌"
        print(f"{status} {username} -> {result} (expected: {expected})")

    # Test national ID validation
    print("\n🆔 National ID Validation Tests:")
    national_id_cases = [
        ("29812251234567", True),  # Valid
        ("2981225123456", False),  # Too short
        ("298122512345678", False),  # Too long
        ("2981225AB34567", False),  # Contains letters
        ("19812251234567", False),  # Invalid century
        ("29813251234567", False),  # Invalid month
        ("29812323234567", False),  # Invalid day
        ("29812380034567", False),  # Invalid governorate
        ("", False),  # Empty
        (None, False)  # None
    ]

    for national_id, expected in national_id_cases:
        result = UserValidation.validate_national_id(national_id)
        status = "✅" if result == expected else "❌"
        print(f"{status} {national_id} -> {result} (expected: {expected})")