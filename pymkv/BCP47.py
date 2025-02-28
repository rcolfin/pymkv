import warnings
from functools import cache

import bcp47


@cache
def is_bcp47(language_ietf: str) -> bool:
    """
    Check if a given language tag is a valid BCP 47 language tag.

    Parameters
    ----------
    language_ietf : str
        The language tag to check.

    Returns
    -------
    bool
        True if the language tag is a valid BCP 47 language tag, False otherwise.
    """
    warnings.warn(
        "The function 'is_bcp47' is deprecated and will be removed in a future release.",
        category=DeprecationWarning,
        stacklevel=2,
    )
    if language_ietf != "und":
        return language_ietf in bcp47.languages.values()
    else:  # noqa: RET505
        return True
