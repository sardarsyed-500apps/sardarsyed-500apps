true, false = True, False

payload = {
    "fields": [
        {
            "attachment": {
                "href": "https://www.youtube.com/watch?v=Uui3oT-XBxs",
                "properties": {
                    "description": "Typeform Home documentary"
                },
                "scale": 0.8,
                "type": "video"
            },
            "id": "A55wpVTUux35",
            "properties": {
                "description": "Cool description for the date",
                "separator": "-",
                "structure": "DDMMYYYY"
            },
            "ref": "nice_readable_date_reference",
            "title": "Date Title",
            "type": "date",
            "validations": {
                "required": false
            }
        },
        {
            "id": "6NA50WpKBkQH",
            "layout": {
                "attachment": {
                    "href": "https://images.typeform.com/images/dr2QKSPuU2RE",
                    "type": "image"
                },
                "placement": "right",
                "type": "float"
            },
            "properties": {
                "alphabetical_order": false,
                "choices": [
                    {
                        "id": "dnAhI6M1RGTw",
                        "label": "Foo",
                        "ref": "01F9KRW5N398ZQP01HDNZRMS7W"
                    },
                    {
                        "id": "5EaniQwPmzf7",
                        "label": "Bar",
                        "ref": "01F9KRW5N3J6MF59P7JXVSZTV5"
                    }
                ],
                "description": "Cool description for the dropdown",
                "randomize": false
            },
            "ref": "nice_readable_dropdown_reference",
            "title": "Dropdown Title",
            "type": "dropdown",
            "validations": {
                "required": false
            }
        },
        {
            "attachment": {
                "href": "https://www.youtube.com/watch?v=Uui3oT-XBxs",
                "scale": 0.8,
                "type": "video"
            },
            "id": "CzHfM8BhYKyI",
            "properties": {
                "description": "Cool description for the email"
            },
            "ref": "nice_readable_email_reference",
            "title": "Email Title",
            "type": "email",
            "validations": {
                "required": false
            }
        },
        {
            "id": "F2vllhXxp63G",
            "properties": {
                "description": "Cool description for the legal"
            },
            "ref": "nice_readable_legal_reference",
            "title": "Legal Title",
            "type": "legal",
            "validations": {
                "required": false
            }
        },
        {
            "id": "dGaVtRi65TlZ",
            "layout": {
                "attachment": {
                    "href": "https://images.typeform.com/images/dr2QKSPuU2RE",
                    "type": "image"
                },
                "type": "wallpaper"
            },
            "properties": {
                "description": "Cool description for the long text"
            },
            "ref": "nice_readable_long_text_reference",
            "title": "Long Text Title",
            "type": "long_text",
            "validations": {
                "max_length": 20,
                "required": false
            }
        },
        {
            "attachment": {
                "href": "https://www.youtube.com/watch?v=Uui3oT-XBxs",
                "scale": 0.8,
                "type": "video"
            },
            "id": "eeIl7VOm5taO",
            "properties": {
                "allow_multiple_selection": false,
                "allow_other_choice": true,
                "choices": [
                    {
                        "id": "16A5s7ywatuE",
                        "label": "Foo",
                        "ref": "foo_choice_ref"
                    },
                    {
                        "id": "FYtuEykT56Qe",
                        "label": "Bar",
                        "ref": "bar_choice_ref"
                    }
                ],
                "description": "Cool description for the multiple choice",
                "randomize": true,
                "vertical_alignment": false
            },
            "ref": "nice_readable_multiple_choice_reference",
            "title": "Multiple Choice Title",
            "type": "multiple_choice",
            "validations": {
                "required": false
            }
        },
        {
            "id": "WkOnxVnetEKM",
            "properties": {
                "allow_multiple_selection": false,
                "choices": [
                    {
                        "id": "xue4zpPevnXP",
                        "label": "Foo",
                        "ref": "foo_choice_ref"
                    },
                    {
                        "id": "m2Im0E4cgWfY",
                        "label": "Bar",
                        "ref": "bar_choice_ref"
                    }
                ],
                "description": "Description for the ranking",
                "randomize": true
            },
            "ref": "nice_readable_ranking_reference",
            "title": "Ranking Title",
            "type": "ranking",
            "validations": {
                "required": false
            }
        },
        {
            "attachment": {
                "href": "https://images.typeform.com/images/dr2QKSPuU2RE",
                "properties": {
                    "description": "A beautiful sunset"
                },
                "type": "image"
            },
            "id": "ZrTDbhcxW179",
            "properties": {
                "description": "Cool description for the number"
            },
            "ref": "nice_readable_number_reference",
            "title": "Number Title",
            "type": "number",
            "validations": {
                "max_value": 50,
                "min_value": 20,
                "required": false
            }
        },
        {
            "attachment": {
                "href": "https://www.youtube.com/watch?v=Uui3oT-XBxs",
                "scale": 0.8,
                "type": "video"
            },
            "id": "3OKqj85EnKvb",
            "properties": {
                "description": "Cool description for the opinion scale field",
                "labels": {
                    "center": "center label",
                    "left": "left label",
                    "right": "right label"
                },
                "start_at_one": true,
                "steps": 9
            },
            "ref": "nice_readable_opinion_scale_reference",
            "title": "Opinion Scale Title",
            "type": "opinion_scale",
            "validations": {
                "required": false
            }
        },
        {
            "id": "l0StviWHDTpp",
            "properties": {
                "allow_multiple_selection": false,
                "allow_other_choice": true,
                "choices": [
                    {
                        "attachment": {
                            "href": "https://images.typeform.com/images/dr2QKSPuU2RE",
                            "properties": {
                                "description": "A sports car"
                            },
                            "type": "image"
                        },
                        "id": "n9k051QYQSza",
                        "label": "Foo 1",
                        "ref": "foo_choice_ref1"
                    },
                    {
                        "attachment": {
                            "href": "https://images.typeform.com/images/dr2QKSPuU2RE",
                            "properties": {
                                "description": "A pickup truck"
                            },
                            "type": "image"
                        },
                        "id": "RE5fwho2Jjzv",
                        "label": "Foo 2",
                        "ref": "foo_choice_ref2"
                    }
                ],
                "description": "Cool description for the picture choice",
                "randomize": true,
                "show_labels": false,
                "supersized": false
            },
            "ref": "nice_readable_picture_choice_reference",
            "title": "Picture Choice Title",
            "type": "picture_choice",
            "validations": {
                "required": false
            }
        }
    ],
    "settings": {
        "are_uploads_public": false,
        "capabilities": {
            "e2e_encryption": {
                "enabled": false,
                "modifiable": false
            }
        },
        "hide_navigation": false,
        "is_public": true,
        "is_trial": false,
        "language": "en",
        "meta": {
            "allow_indexing": false
        },
        "progress_bar": "proportion",
        "show_progress_bar": true,
        "show_time_to_complete": true,
        "show_typeform_branding": true
    },
    "thankyou_screens": [
        {
            "properties": {
                "share_icons": false,
                "show_button": false
            },
            "ref": "default_tys",
            "title": "Done! Your information was sent perfectly."
        }
    ],
    "theme": {
        "href": "https://api.typeform.com/themes/qHWOQ7"
    },
    "title": "Sardar's Second example form",
    "type": "form",
    "workspace": {
        "href": "https://api.typeform.com/workspaces/kZVT2C"
    }
}


payload = [{
            "attachment": {
                "href": "https://www.youtube.com/watch?v=Uui3oT-XBxs",
                "properties": {
                    "description": "Typeform Home documentary"
                },
                "scale": 0.8,
                "type": "video"
            },
            "id": "A55wpVTUux35",
            "properties": {
                "description": "Cool description for the date",
                "separator": "-",
                "structure": "DDMMYYYY"
            },
            "ref": "nice_readable_date_reference",
            "title": "Date Title",
            "type": "date",
            "validations": {
                "required": false
            }
        },
        {
            "id": "WkOnxVnetEKM",
            "properties": {
                "allow_multiple_selection": false,
                "choices": [
                    {
                        "id": "xue4zpPevnXP",
                        "label": "Foo",
                        "ref": "foo_choice_ref"
                    },
                    {
                        "id": "m2Im0E4cgWfY",
                        "label": "Bar",
                        "ref": "bar_choice_ref"
                    }
                ],
                "description": "Description for the ranking",
                "randomize": true
            },
            "ref": "nice_readable_ranking_reference",
            "title": "Ranking Title",
            "type": "ranking",
            "validations": {
                "required": false
            }
        }
]

def remove_field(pl, key):
    """Remove items with given key in any dict at any level in the nested dict/list/tuple"""

    if type(pl) is tuple:
        r = (remove_field(v, key) for v in pl)

    elif type(pl) is list:
        r = [remove_field(v, key) for v in pl]
        
    elif type(pl) is dict:
        r = {k: remove_field(v, key) for (k, v) in pl.items() if k != key}
    else: 
        r = pl

    return r


from icecream import ic

payload = remove_field(payload, 'id')

