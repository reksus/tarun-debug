pex_binary(
    name="manage",
    entry_point="manage.py",
    dependencies=[
        "./proj1:settings",
    ],
    restartable=True,
)

python_sources()


python_awslambda(
    name="lambda",
    runtime="python3.9",
    dependencies=[
        "./proj1:settings",
    ],
    handler="proj1/wsgi.py:lambda_handler",
)
