from marshmallow import validate, Schema, fields

class BrokerOutputSchema(Schema):
    id = fields.Int(required=True)
    agency_id = fields.Int(required=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)

broker_output_schema = BrokerOutputSchema(strict=True)


class BrokerInputSchema(Schema):
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)

broker_input_schema = AgencyInputSchema(strict=True)
