class User:
  def __init__(self, username, password, id):
    self._password = password
    self._name = username
    self._id = id

  
  @property
  def name(self):
    return self._name

  
  @property
  def password(self):
    return self._password

  
  @property
  def id(self):
    return self._id

  
  @name.setter
  def name(self, username):
    self._name = username
    

  @password.setter
  def password(self, password):
    self._password = password

  
  @id.setter
  def id(self, id):
    self._id = id
    

  def __str__(self):
    return self.name