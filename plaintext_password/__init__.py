from django.contrib.auth.hashers import BasePasswordHasher, mask_hash
from django.utils.translation import gettext_noop as _

from . import checks  # noqa


class PlaintextPasswordHasher(BasePasswordHasher):
    """
    Password hashing, without the hashing.

    Store passwords in plaintext.
    """

    algorithm = "plaintext"

    def salt(self) -> str:
        return ""

    def decode(self, encoded):
        return {
            "algorithm": self.algorithm,
            "hash": encoded,
            "salt": None,
        }

    def harden_runtime(self, password, encoded):
        pass

    def safe_summary(self, encoded):
        decoded = self.decode(encoded)
        return {
            _("algorithm"): decoded["algorithm"],
            _("hash"): mask_hash(decoded["hash"], show=3),
        }

    def encode(self, password: str, salt: str):
        assert salt == ""
        return f"{self.algorithm}$${password}"

    def verify(self, password: str, encoded: str) -> bool:
        """
        Constant-time comparison? What's that?
        """
        return encoded == self.encode(password, "")


__all__ = ["PlaintextPasswordHasher"]
