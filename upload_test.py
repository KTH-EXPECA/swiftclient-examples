from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient.client import Connection

# Create a password auth plugin
auth = v3.Password(auth_url='http://10.0.87.254:5000/v3/',
                   username='admin',
                   password='wcXLR6yAZ6mya79vi1BkjtIkONHyZqO9kJg0tYOp',
                   user_domain_name='Default',
                   project_name='openstack',
                   project_domain_name='Default')

# Create session
keystone_session = session.Session(auth=auth)

# Create swiftclient Connection
conn = Connection(session=keystone_session)

container = 'students-project'
with open('test.txt', 'rb') as f:
    file_data = f.read()
    conn.put_object(
        container,
        'test.txt',
        contents=file_data,
    )
