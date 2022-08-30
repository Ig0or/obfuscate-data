valid_input_list = ["value", 1, 2, 3, 4, 8.2]
encoded_valid_list = ['fca12ad963', '301292c073', '9a7145e0f4', '2c9766fa2d', '193fb5e7c4', '206a2c3dd4']

valid_input_dict = {
    "first key": "first value",
    "second key": "second value",
    "third key": "third value",
}
encoded_valid_dict = {'first key': 'e752960844', 'second key': '31f7fa073c', 'third key': 'ee2c17a124'}


valid_great_dict = {
    "first key": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "second key": {
        "children one": [
            {"children one": [1, 2, "string"]},
            "string",
            [
                {"key": "value", "key2:": "value2", "key3": {"key": "value"}},
                2,
                3,
                "string",
                5,
                6,
                7,
            ],
        ]
    },
}
encoded_valid_great_dict = {'first key': ['301292c073', '9a7145e0f4', '2c9766fa2d', '193fb5e7c4', 'b41aa9c083', '31eb4c9a88', '9114200cf7', '1212c5a411', '6cc5ab416d', 'a78ec3a83b'], 'second key': {'children one': [{'children one': ['301292c073', '9a7145e0f4', '612396e5a9']}, '612396e5a9', [{'key': 'fca12ad963', 'key2:': '49ae1f4f38', 'key3': {'key': 'fca12ad963'}}, '9a7145e0f4', '2c9766fa2d', '612396e5a9', 'b41aa9c083', '31eb4c9a88', '9114200cf7']]}}

invalid_input_list = [callable]
invalid_input_dict = {"key": callable}
