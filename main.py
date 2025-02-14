import re


# 1 Email Addresses
def extract_email(outcome):
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(email_regex, outcome)


# 2 URLS
def extract_url(outcome):
    url_regex = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    return re.findall(url_regex, outcome)


# 3 Phone Numbers
def extract_phone_numbers(outcome):
    phone_numbers_regex = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
    return re.findall(phone_numbers_regex, outcome)


# 4 Credit Card
def extract_credit_card(outcome):
    credit_card_regex = r"\b(?:\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}|\d{16})\b"
    return re.findall(credit_card_regex, outcome)


# Test the Functions
def test_regex():

    # Test Strings Outcome

    test_email = "m.ahol@alustudent.com"
    test_url = "https://intranet.aluswe.com/projects/current"
    test_phone_number = "0794423393"
    test_credit_card = "465-687-830-270"

    # Extract Data Outcome

    print(f"Monica Akoi extract email: \n{test_email}\n")
    print(f"ALU Intranet Site: \n{test_url}\n")
    print(f"Myphone number: \n{test_phone_number}\n")
    print(f"Credit card: \n{test_credit_card}\n")


if __name__ == "__main__":
    test_regex()



