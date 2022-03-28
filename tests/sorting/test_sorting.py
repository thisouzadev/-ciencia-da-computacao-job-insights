from src.sorting import sort_by

mock = [
    {"max_salary": 100000, "min_salary": 50000, "date_posted": "2021-05-24"},
    {"max_salary": 1000, "min_salary": 500000, "date_posted": "2021-05-23"},
    {"max_salary": 1000000, "min_salary": 5000, "date_posted": "2021-05-28"},
    {"max_salary": 100, "min_salary": 50, "date_posted": "2021-05-21"},
    {"max_salary": 10000, "min_salary": 500, "date_posted": "2021-05-28"},
]

min_salary_sort_by_crescent = [mock[3], mock[4], mock[2], mock[0], mock[1]]
max_salary_sort_by_decrescent = [mock[2], mock[0], mock[4], mock[1], mock[3]]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == min_salary_sort_by_crescent
    sort_by(mock, "max_salary")
    assert mock == max_salary_sort_by_decrescent
