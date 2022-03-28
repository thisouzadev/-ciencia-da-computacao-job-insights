from src.jobs import read


def get_unique_job_types(path):
    jobs_file = read(path)
    job_types = set()

    for job in jobs_file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    job_filter = list()

    for job in jobs:
        if job["job_type"] == job_type:
            job_filter.append(job)
    return job_filter


def get_unique_industries(path):
    infos = read(path)
    unique_industries = set()
    for industry in infos:

        if industry['industry'] != '':
            unique_industries.add(industry['industry'])
    return unique_industries


def filter_by_industry(jobs, industry):
    industry_filter = list()
    for job in jobs:
        if job["industry"] == industry:
            industry_filter.append(job)
    return industry_filter


def get_max_salary(path):
    jobs_file = read(path)
    max_salary = set()
    for job in jobs_file:
        if job["max_salary"].isnumeric():
            max_salary.add(int(job["max_salary"]))
    return max(list(max_salary))


def get_min_salary(path):
    jobs_file = read(path)
    min_salary = set()
    for job in jobs_file:
        # The isnumeric() method returns:
        # True if all characters in the string are numeric characters.
        # False if at least one character is not a numeric character.
        if job["min_salary"].isnumeric():
            min_salary.add(int(job["min_salary"]))
    return min(list(min_salary))


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
        # If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        # Use the int() Function to Check if the Input Is an Integer in Python.
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
        # If `job["min_salary"]` is greather than `job["max_salary"]`
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
        # If `salary` isn't a valid integer
    if type(salary) != int:
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    job_filter = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_filter.append(job)
        except ValueError:
            pass
    return job_filter
