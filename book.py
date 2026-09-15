from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def add_record(self, record:Record) -> Record | None:
        self.data[record.name.value]=record
    
    def find(self, name: str) -> Record:
        return self.data.get(name)
    
    def delete(self, name) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Запис {name} не знайдено")
    
    def __str__(self) ->str:
        result=''
        for name, record in self.data.items():
            result+=str(record)+'\n'
        return result.strip()