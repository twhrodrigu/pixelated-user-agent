from mock import Mock
from datetime import datetime

LEAP_FLAGS = ['\\Seen',
              '\\Answered',
              '\\Flagged',
              '\\Deleted',
              '\\Draft',
              '\\Recent',
              'List']


def leap_mail(uid=0, leap_flags=LEAP_FLAGS, extra_flags=[], headers={'date': str(datetime.now())}):
    flags = leap_flags + extra_flags
    return Mock(getUID=Mock(return_value=uid),
                getFlags=Mock(return_value=flags),
                bdoc=Mock(content={'raw': 'test'}),
                hdoc=Mock(content={'headers': headers}))
