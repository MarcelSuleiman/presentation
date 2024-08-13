import pydantic


class Model(pydantic.BaseModel):
    class Config:
        populate_by_name = True
        extra = 'allow'
        use_enum_values = True
