class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def test_team_lead():
    lead = TeamLead("Дима", 5000, "IT отдел", "Python", 5)

    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")
    assert hasattr(lead, "department")
    assert hasattr(lead, "programming_language")
    assert hasattr(lead, "team_size")