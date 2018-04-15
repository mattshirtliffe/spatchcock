from marshmallow import Schema, fields, post_load


class CrimeSchema(Schema):
    crime_id = fields.Str(required=True)
    month = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()
    location = fields.Str()
    category = fields.Str()
    outcome_status = fields.Str()