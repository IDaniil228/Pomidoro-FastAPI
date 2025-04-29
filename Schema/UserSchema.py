from pydantic import BaseModel, Field, model_validator

class UserSchema(BaseModel):
    id : int
    name : str = Field(max_length=256)
    second_name : str = Field(max_length=256)
    age : int

    class Config:
        from_attributes = True

    def __str__(self):
        return f"id - {self.id}  Имя - {self.name} возраст - {self.age}"

    @model_validator(mode="after")
    def check_correct_data(self):
        if self.age <= 0 or self.age > 120:
            raise ValueError("Некорректный возраст")
        return self



