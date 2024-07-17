from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError


class Address(BaseModel):
    city: str = Field(min_length=2, description="The city name must be minimum 2 symbols")
    street: str = Field(min_length=3, description="The street name must be minimum 3 symbols")
    house_number: int = Field(gt=0, description="The house_number must be positive number")


class User(BaseModel):
    name: str = Field(min_length=2, description="The name must be minimum 2 symbols")
    age: int = Field(gt=0, lt=120, description="The age must be between 0 and 120")
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator('name')
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only letters')
        return value

    @field_validator("is_employed")
    def validate_age_is_employed(cls, value, values):
        age = values.data.get('age')
        if value and age is not None and age < 18:
            raise ValueError("User must be employed at least 18 years old")
        return value


def json_serialize_deserialize(json_string):
    try:
        user = User.parse_raw(json_string)
        return user.json()
    except ValidationError as e:
        print("Validation error:", e)


json_string1 = """{
    "name": "Bob",
    "age": 30,
    "email": "bobmar@example.com",
    "is_employed": true,
    "address": {
        "city": "Boston",
        "street": "7th Solar",
        "house_number": 17
    }
}"""

json_string2 = """{
    "name": "Marley",
    "age": 15,
    "email": "mar@example.com",
    "is_employed": true,
    "address": {
        "city": "London",
        "street": "11th Moon",
        "house_number": 52
    }
}"""


print(json_serialize_deserialize(json_string1))
print(json_serialize_deserialize(json_string2))