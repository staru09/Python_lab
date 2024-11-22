class Instructor:
    def __init__(self, name, experience, avg_feedback, technology_skills):
        
        self.__name = name
        self.__experience = experience
        self.__avg_feedback = avg_feedback
        self.__technology_skills = technology_skills

   
    def set_name(self, name):
        self.__name = name

    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def set_technology_skills(self, technology_skills):
        self.__technology_skills = technology_skills

 
    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def get_technology_skills(self):
        return self.__technology_skills

    
    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4.0:
            return True
        return False

   
    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skills:
            return True
        return False


if __name__ == "__main__":
   
    instructor1 = Instructor("Alice", 5, 4.6, ["Python", "Java"])
    instructor2 = Instructor("Bob", 2, 4.2, ["C++", "JavaScript"])
    instructor3 = Instructor("Charlie", 3, 3.9, ["Python", "HTML"])

    print(f"{instructor1.get_name()} eligibility: {instructor1.check_eligibility()}")
    print(f"{instructor2.get_name()} eligibility: {instructor2.check_eligibility()}")
    print(f"{instructor3.get_name()} eligibility: {instructor3.check_eligibility()}")

   
    print(f"{instructor1.get_name()} course allocation for Python: {instructor1.allocate_course('Python')}")
    print(f"{instructor2.get_name()} course allocation for Java: {instructor2.allocate_course('Java')}")
    print(f"{instructor3.get_name()} course allocation for HTML: {instructor3.allocate_course('HTML')}")
