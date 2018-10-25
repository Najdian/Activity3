class Udacian:
  def __init__(self, name, city, enrollment, nanodegree, status):
    self.name = name
    self.city = city
    self.enrollment = enrollment
    self.nanodegree = nanodegree
    self.status = status


student = Udacian("Abdullah", "Riyadh", "Virtual", "Full Stack Development", "On Track")

print(student.name, student.city, student.enrollment, student.nanodegree, student.status)