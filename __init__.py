from rbitra.org_utils import add_member_to_org_by_uuid
import marshmallow

details = {
    'title': 'Meta Plugin',
    'uuid': 'e64ca948-c380-4339-8263-a27c29d83a0f',
    'module_name': 'meta_plugin',
    'class_name': 'MetaPlugin'
}

def add_member_to_org(arguments):
    add_member_to_org_by_uuid(arguments["member"], arguments["org"])

class AddMemberToOrgArgSchema(marshmallow.Schema):
    member = marshmallow.fields.UUID()
    org = marshmallow.fields.UUID()

    @marshmallow.validates('member')
    def check_member(self, uuid):
        try:
            assert Member.query.filter_by(uuid=uuid).first() is not None
        except AssertionError:
            raise marshmallow.ValidationError("Member UUID invalid.")

    @marshmallow.validates('org')
    def check_org(self, uuid):
        try:
            assert Organization.query.filter_by(uuid=uuid).first() is not None
        except AssertionError:
            raise marshmallow.ValidationError("Org UUID invalid.")


valid_actions = {
    "add_member_to_org": {
        "description": "Add Member to Organization",
        "arg_schema": AddMemberToOrgArgSchema,
        "action": add_member_to_org
        "mod_role_req": True
    }
}

