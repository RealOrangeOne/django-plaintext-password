from django.conf import settings
from django.contrib.auth.hashers import get_hashers_by_algorithm
from django.core import checks


@checks.register(checks.Tags.security)
def check_for_plaintext_passwords(app_configs, **kwargs):
    if not settings.DEBUG and "plaintext" in get_hashers_by_algorithm():
        yield checks.Critical(
            "Plaintext module should not be used in production.", hint="Remove it."
        )
