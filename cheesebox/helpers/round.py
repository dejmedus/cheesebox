
def round_result(result):
    if isinstance(result, float):
        return f"{format(result, '.2f').rstrip('0').rstrip('.')}"
    else:
        return result