
def auto_differentiate (unverified_form) :
    if (len(unverified_form.JobTitle) < 3) and (len(unverified_form.JobTitle) > 30):
        return False
    if (len(unverified_form.Company) < 3) and (len(unverified_form.JobTitle) > 30):
        return False
    if (len(unverified_form.Location) < 3) and (len(unverified_form.Location) > 30):
        return False
    if (unverified_form.Salary < 0) and (unverified_form.Salary > 200000):
        return False
    if (unverified_form.JobDescription == None):
        return False
    return True