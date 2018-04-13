from marshmallow import Schema, fields

class CrimeSchema(Schema):
    crime_id = fields.Str()
    month = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()
    location = fields.Str()
    category = fields.Str()
    outcome_status = fields.Str()