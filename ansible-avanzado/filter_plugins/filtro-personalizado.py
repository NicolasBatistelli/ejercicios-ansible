# filter_plugins/custom_filters.py
def reverse_string(value):
    """Reverse a string."""
    return value[::-1]

class FilterModule(object):
    def filters(self):
        return {
            'reverse_string': reverse_string
        }

