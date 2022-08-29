pex_binary(
    name="django-admin",
    dependencies=[
        ":poetry#Django",
    ],
    script="django-admin",
)


poetry_requirements(
    name="poetry",
    module_mapping={
        "python-decouple": ["decouple"],
        "djangorestframework": ["rest_framework"],
    },
)