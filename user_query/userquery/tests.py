from django.core.urlresolvers import resolve
from rest_framework.test import APITestCase, APIRequestFactory


class UserQueryAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_list_userquery_routes(self):
        route = resolve('/userquery/')
        self.assertEqual(route.func.__name__, 'QueryViewSet')

    def test_list_userquery(self):
        response = self.client.get('/userquery/')
        self.assertEqual(response.status_code, 200)

    def test_create_userquery(self):
        # put new userquery
        queryName = 'query1'
        post_data = {
            'name': queryName,
            'description': 'query1 description',
            'query': 'select 1',
            'tablename': 'table_name',
            'is_public': True,
        }

        response = self.client.post('/userquery/', post_data, format='json')
        self.assertEqual(response.status_code, 201)

        # return new userquery list
        response = self.client.get('/userquery/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], queryName)

        # change userquery name
        queryName = 'newquery1'
        put_data = {'name': queryName}
        response = self.client.put('/userquery/1/', put_data, format='json')
        self.assertEqual(response.status_code, 200)

        # return new userquery list
        response = self.client.get('/userquery/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], queryName)

        # delete query
        response = self.client.delete('/userquery/1/')
        self.assertEqual(response.status_code, 204)

        # return new userquery list - (return 0 userqueries)
        response = self.client.get('/userquery/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)