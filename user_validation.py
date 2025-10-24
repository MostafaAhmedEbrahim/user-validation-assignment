import re


class UserValidation:

    @staticmethod
    def validate_email(email: str) -> bool:
        if email is None:
            return False

        if not isinstance(email, str) or email.strip() == "":
            return False

        pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email) and ' ' not in email:
            return True

        return False

    @staticmethod
    def validate_username(username: str) -> bool:
        if username is None:
            return False

        if not isinstance(username, str):
            return False

        if len(username) < 3 or len(username) > 20:
            return False

        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False

        return True

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        if phone is None:
            return False

        if not isinstance(phone, str):
            return False

        phone = phone.replace(' ', '').replace('-', '')

        if not phone.isdigit():
            return False

        if len(phone) == 11:
            valid_prefixes = ['010', '011', '012', '015']
            return phone[:3] in valid_prefixes

        elif len(phone) == 12:
            if phone.startswith('20'):
                operator_code = phone[2:4]
                valid_operator_codes = ['10', '11', '12', '15']
                return operator_code in valid_operator_codes

        return False

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        if national_id is None:
            return False

        if not isinstance(national_id, str):
            return False

        if len(national_id) != 14 or not national_id.isdigit():
            return False

        century_code = national_id[0]
        month = national_id[3:5]
        day = national_id[5:7]
        governorate_code = national_id[7:9]

        if century_code not in ['2', '3']:
            return False

        if not (1 <= int(month) <= 12):
            return False

        if not (1 <= int(day) <= 31):
            return False

        month_int = int(month)
        day_int = int(day)

        if month_int in [4, 6, 9, 11] and day_int > 30:
            return False

        if month_int == 2 and day_int > 29:
            return False

        governorate_num = int(governorate_code)
        if not (1 <= governorate_num <= 88):
            return False

        return True


if __name__ == "__main__":
    print("=== Testing UserValidation Class ===")

    print("\nEmail Validation Tests:")
    email_cases = [
        ("mostafa.ahmed@example.com", True),
        ("mostafaexample.com", False),
        ("mostafa@", False),
        ("mostafa@mail.c", False),
        ("mostafa@mail.company.com", True),
        ("mostafa.ahmed_21@mail.co", True),
        ("MOSTAFA@MAIL.COM", True),
        ("mostafa ahmed@mail.com", False),
        ("", False),
        (None, False)
    ]

    for email, expected in email_cases:
        result = UserValidation.validate_email(email)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} {email} -> {result} (expected: {expected})")

    print("\nPhone Number Validation Tests:")
    phone_cases = [
        ("01012345678", True),
        ("01234567890", True),
        ("01198765432", True),
        ("01555555555", True),
        ("201012345678", True),
        ("201112345678", True),
        ("201212345678", True),
        ("201512345678", True),
        ("01812345678", False),
        ("0101234567", False),
        ("010123456789", False),
        ("01012abc678", False),
        ("", False),
        (None, False)
    ]

    for phone, expected in phone_cases:
        result = UserValidation.validate_phone_number(phone)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} {phone} -> {result} (expected: {expected})")

    print("\nUsername Validation Tests:")
    username_cases = [
        ("mostafa_ahmed", True),
        ("mo", False),
        ("mostafaahmedverylongusername", False),
        ("mostafa ahmed", False),
        ("mostafa@123", False),
        ("mostafa123", True),
        ("", False),
        (None, False)
    ]

    for username, expected in username_cases:
        result = UserValidation.validate_username(username)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} {username} -> {result} (expected: {expected})")

    print("\nNational ID Validation Tests:")
    national_id_cases = [
        ("29812251234567", True),
        ("2981225123456", False),
        ("298122512345678", False),
        ("2981225AB34567", False),
        ("19812251234567", False),
        ("29813251234567", False),
        ("29812323234567", False),
        ("29812380034567", False),
        ("", False),
        (None, False)
    ]

    for national_id, expected in national_id_cases:
        result = UserValidation.validate_national_id(national_id)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} {national_id} -> {result} (expected: {expected})")
