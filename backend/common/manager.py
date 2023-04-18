from abc import *

# class ManagerBase(metaclass=ABCMeta):
#     pass
    

# class Manager(ManagerBase):
#     pass
    

# class MakeManager(Manager):
#     pass
    
# class GetManager(Manager):
#     pass

# class APIManager(ManagerBase):
# 아마 로그처럼 띄윚 않을까 싶다.
#     pass

class ManagerBase(metaclass=ABCMeta):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def get_data(self):
        return self.data