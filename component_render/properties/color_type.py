from enum import Enum

class ColorType(Enum):
  NEUTRAL_STRONG = 'neutralStrong',
  NEUTRAL_MEDIUM = 'neutralMedium',
  NEUTRAL_WEAK = 'neutralWeak',
  NEUTRAL_SUBTLE = 'neutralSubtle',
  NEUTRAL_INVERSE = 'neutralInverse',
  PRIMARY = 'primary',
  PRIMARY_WEAK = 'primaryWeak',
  POSITIVE = 'positive',
  POSITIVE_WEAK = 'positiveWeak',
  NOTICE = 'notice',
  NOTICE_WEAK = 'noticeWeak',
  NEGATIVE = 'negative',
  NEGATIVE_WEAK = 'negativeWeak',
  OFFSET_STRONG = 'offsetStrong',
  OFFSET_MEDIUM = 'offsetMedium',
  OFFSET_WEAK = 'offsetWeak',