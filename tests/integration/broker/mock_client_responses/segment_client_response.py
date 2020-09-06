from asynctest import CoroutineMock
from starlette import status

MOCK_GET_CATALOG_CONSUMER_SUCCESS_RESPONSE = {"name": "consumer",
                                              "options": [{
                                                  "id": 24,
                                                  "name": "alcohol",
                                                  "description": "Alcohol",
                                                  "options": []
                                              },
                                                  {
                                                      "id": 1,
                                                      "name": "automotive",
                                                      "description": "Automotive",
                                                      "options": []
                                                  },
                                                  {
                                                      "id": 25,
                                                      "name": "commuting-and-transportation",
                                                      "description": "Commuting and Transportation",
                                                      "options": []
                                                  }
                                              ]}

MOCK_GET_ALL_CATALOG_SUCCESS_RESPONSE = {"name": "catalog",
                                         "options": [
                                             {
                                                 "name": "Demographics",
                                                 "options": [
                                                     {
                                                         "name": "Gender",
                                                         "options": [
                                                             {
                                                                 "tag": "male",
                                                                 "description": "Male"
                                                             },
                                                             {
                                                                 "tag": "female",
                                                                 "description": "Female"
                                                             }
                                                         ]
                                                     },
                                                     {
                                                         "name": "Age",
                                                         "options": [
                                                             {
                                                                 "tag": "a05p",
                                                                 "description": "Persons 5+ yrs"
                                                             },
                                                             {
                                                                 "tag": "a16p",
                                                                 "description": "Persons 16+ yrs"
                                                             }
                                                         ]
                                                     }
                                                 ]
                                             }
                                         ]
                                         }

MOCK_GET_FILTER_SEGMENT_SUCCESS_RESPONSE = {
    "segment_id": 9188,
    "next_tags": [
        "a18p"
    ]
}

MOCK_GET_CATALOG_POP_FACTS_SUCCESS_RESPONSE = {
    "name": "catalog",
    "options": {
        "name": "catalog",
        "options": [
            {
                "name": "Demographics",
                "options": [
                    {
                        "name": "Gender",
                        "options": [
                            {
                                "tag": "male",
                                "description": "Male"
                            },
                            {
                                "tag": "female",
                                "description": "Female"
                            }
                        ]
                    },
                    {
                        "name": "Age",
                        "options": [
                            {
                                "tag": "a05p",
                                "description": "Persons 5+ yrs"
                            },
                            {
                                "tag": "a16p",
                                "description": "Persons 16+ yrs"
                            },
                            {
                                "tag": "a18p",
                                "description": "Persons 18+ yrs"
                            },
                            {
                                "tag": "a18t34",
                                "description": "Persons 18-34 yrs"
                            },
                            {
                                "tag": "a18t49",
                                "description": "Persons 18-49 yrs"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}


def set_mock_get_consumer_catalog_success_case(mock_post):
    mock_post.return_value.__aenter__.return_value.status = status.HTTP_200_OK
    mock_post.return_value.__aenter__.return_value.json = CoroutineMock(
        return_value=MOCK_GET_CATALOG_CONSUMER_SUCCESS_RESPONSE
    )


def set_mock_get_all_catalog_success_case(mock_post):
    mock_post.return_value.__aenter__.return_value.status = status.HTTP_200_OK
    mock_post.return_value.__aenter__.return_value.json = CoroutineMock(
        return_value=MOCK_GET_ALL_CATALOG_SUCCESS_RESPONSE
    )


def set_mock_get_filter_segment_success_case(mock_post):
    mock_post.return_value.__aenter__.return_value.status = status.HTTP_200_OK
    mock_post.return_value.__aenter__.return_value.json = CoroutineMock(
        return_value=MOCK_GET_FILTER_SEGMENT_SUCCESS_RESPONSE
    )


def set_mock_get_pop_facts_catalog_success_case(mock_post):
    mock_post.return_value.__aenter__.return_value.status = status.HTTP_200_OK
    mock_post.return_value.__aenter__.return_value.json = CoroutineMock(
        return_value=MOCK_GET_CATALOG_POP_FACTS_SUCCESS_RESPONSE
    )
