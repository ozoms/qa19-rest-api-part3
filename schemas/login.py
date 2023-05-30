from voluptuous import PREVENT_EXTRA, Schema

login = Schema(
    {
        "token": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)
