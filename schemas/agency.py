from marshmallow import validate, Schema, fields

from models.agency import Agency


class AgencyOutputSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    domain = fields.Str(required=True)
    address = fields.Str(required=True)

    class Meta:
        model = Agency
        fields = ('id', 'title', 'domain', 'address')


agency_list_output_schema = AgencyOutputSchema(strict=True, many=True)
agency_output_schema = AgencyOutputSchema(strict=True)


class AgencyInputSchema(Schema):
    title = fields.Str(required=True)
    domain = fields.Str(required=True)
    address = fields.Str(required=True)


agency_input_schema = AgencyInputSchema(strict=True)
