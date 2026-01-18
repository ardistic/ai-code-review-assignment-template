# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

EMAIL_REGEX = re.compile(
    r"^(?!\.)(?!.*\.{2})[a-zA-Z0-9._%+-]+(?<!\.)"
    r"@"
    r"[a-zA-Z0-9.-]+"
    r"\.[a-zA-Z]{2,}$"
)

def count_valid_emails(emails):
    valid_count = 0

    for email in emails:
        if not isinstance(email, str) or not EMAIL_REGEX.match(email):
            continue

        _, domain = email.split("@")
        labels = domain.split(".")

        if not any(not l or l.startswith("-") or l.endswith("-") for l in labels):
            valid_count += 1

    return valid_count