# if applicant has high income "AND" good credit
# Eligible for loan
# AND: both

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan :)")

###########################################

# if applicant has high income "OR" good credit
# Eligible for loan
# OR: at least one

print(15 * '*')

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan :)")

###########################################

# if applicant has good credit AND doesn't have a criminal record
# Eligible for loan

print(15 * '*')

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan :)")
