#!/usr/bin/env python


import string

from cloudant.client import Cloudant



client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                  "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                  url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
client.connect()
def add_signal(status, load):
    client = Cloudant("39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix",
                      "48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff",
                      url="https://39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix:48e26645f504209f85b4c44d74a4cb14bc0d059a22b361534b78f406a513f8ff@39a4348e-3ce1-40cd-b016-1f85569d409e-bluemix.cloudant.com")
    client.connect()


    databaseName = load
    myDatabase = client.create_database(databaseName)
    client.delete_database(databaseName)

    # if myDatabase.exists():
    #     print("'{0}' successfully created.\n".format(databaseName))
    #     client.delete_database(databaseName)
    myDatabase = client.create_database(databaseName)



    sampleData = [
        [ status , "kitchen"]
    ]

    # Create documents using the sample data.
    # Go through each row in the array
    for document in sampleData:
        # Retrieve the fields in each row.
        number = document[0]
        name = document[1]

        # Create a JSON document that represents
        # all the data in the row.
        jsonDocument = {
            "status": number,
            "circuit": name
        }

        # Create a document using the Database API.
        newDocument = myDatabase.create_document(jsonDocument)

        # Check that the document exists in the database.
        if newDocument.exists():
            print("Document '{0}' successfully created.".format(number))
        client.disconnect()
