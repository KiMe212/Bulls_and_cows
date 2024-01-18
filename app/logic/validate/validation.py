def _length(number: str):
    if len(number) > 4:
        return 1


def _similar_number(number: str):
    if len(set(number)) != 4:
        return 1


def _validate_zero(number: str):
    if "0" in number:
        return 1


def _validate_int(number: str):
    if not number.isdigit():
        return 1


def validate(number: str):
    return 1 not in (
        _validate_int(number),
        _validate_zero(number),
        _length(number),
        _similar_number(number),
    )
