import unittest
from main import create_app,db

# The database will need to be re-created and seeded if you choose to delete. 
# Commands to re-seed in the terminal:
# Ensure virtual environment is initiated: source venv/bin/activate
# Create database: flask db create
# Seed database: flask db seed 

class TestUsers(unittest.TestCase):

    word = None
    while word != "yes":
        word = input("\nWould you like to create and seed the database? This only needs to be done "
                    "if the database is empty.\nIf empty the testing may cause an error.\nType yes or no: ")
        word = word.lower()
        print(word)
        if word == "yes":
                @classmethod
                def setUp(cls):
                    cls.app = create_app()
                    cls.app_context = cls.app.app_context()
                    cls.app_context.push()
                    cls.client = cls.app.test_client()
                    db.create_all()

                    runner = cls.app.test_cli_runner()
                    runner.invoke(args=["db", "seed"])
                    print("Database seeded")
        elif word == "no":
            break

        else:
            print("You did not type yes or no correctly. Please ensure correct spelling")
        
    def test_user(self):
        app = create_app()
        client = app.test_client()  # A method given by flask to assist in making http requests.

        # Test GET all data on users has a response of 200 and type dict returned.
        response = client.get("/user/")

        data = response.get_json()

        self.assertEqual(response.status_code,200)
        self.assertIsInstance(data, list)

        # Test GET data on one user with id 1
        response = client.get("/user/1")

        data = response.get_json()

        self.assertEqual(response.status_code,200)
        self.assertIsInstance(data, dict)

        # Test POST response data on create a new user
        response = client.post("/user/create",json={"email":"scott@pot.not",
                                                    "first_name":"Scott",
                                                    "Surname": "Pot",
                                                    "Password": "abcde",
                                                    "Age":27,
                                                    "Address":"123 happy st Mockville",
                                                    "City":"Bangledesh",
                                                    "State":"NSW",
                                                    "Country": "Australia",
                                                    "Postcode": 2345})

        data = response.get_json()
                
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(data, dict)

        # Testing the update returns a 200 and type dict

        response = client.patch("/user/update/2",json={"email":"scott@chop.dop"})

        data = response.get_json()
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(data, dict)

        # Testing the delete user with id 2 returns a 200 
        response = client.delete("/user/delete/2")

        data = response.get_json()
        self.assertEqual(response.status_code,200)
            
    word = None
    while word != "yes":
        word = input("Would you like to delete all the data on the database after this test but before making any other test? Type yes or no: ")
        word = word.lower()
        if word == "yes":
            
            @classmethod
            def tearDown(cls):
                db.session.remove()
                db.drop_all()
                cls.app_context.pop()

        elif word == "no":
            break

        else:
            print("You did not type yes or no correctly. Please ensure correct spelling")











        

        




