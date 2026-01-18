# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    if not emails:
        return 0
        
    count = 0
    for email in emails:
        if isinstance(email, str) and "@" in email:
            count += 1
    return count