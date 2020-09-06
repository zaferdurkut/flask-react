from marshmallow import validate, Schema, fields

class BrokerOutputSchema(Schema):
    id = fields.Int(required=True)
    agency_id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)

broker_output_schema = BrokerOutputSchema(strict=True)
broker_output_list_schema = BrokerOutputSchema(strict=True, many=True)


class BrokerInputSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)

broker_input_schema = BrokerInputSchema(strict=True)
