class IntOrStrConverter:

    regex = '[0-9]+|[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,4}'

    def to_python(self, value):
        if value.isdigit():
            return int(value)
        else:
            return str(value)
        
    def to_url(self, value):
        return str(value)
    

class CategoryNameConverter:
    regex = r'[a-zA-Z]+'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)
