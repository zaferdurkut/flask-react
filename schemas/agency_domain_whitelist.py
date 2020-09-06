from marshmallow import validate, Schema, fields


class AgencyDomainWhitelistSchema(Schema):
    id = fields.Integer(required=True)
    domain = fields.Str(required=True)


agency_domain_whitelist_schema = AgencyDomainWhitelistSchema(strict=True)

agency_domain_whitelist_list_schema = AgencyDomainWhitelistSchema(strict=True, many=True)

class AgencyDomainWhitelistInputSchema(Schema):
    domain = fields.Str(required=True)


agency_domain_whitelist_input_schema = AgencyDomainWhitelistInputSchema(strict=True)
