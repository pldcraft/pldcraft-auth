from sqlalchemy.types import TypeDecorator, Text

import json


class IntTuple(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        assert isinstance(value, tuple)
        assert all(isinstance(i, int) for i in value)

        return json.dumps(list(value))

    def process_result_value(self, value, dialect):
        l = json.loads(value)

        assert isinstance(l, list)
        assert all(isinstance(i, int) for i in l)

        return tuple(l)

