__author__ = 'Stas'


class MetricCommon(object):
    """
    Abstract class (Interface) for any metric class
    """
    metric_type = 'common'

    def __init__(self, auth, initials):
        """
        Initialize Metric
        @param auth: authenticator
        @param initials: some dict with initials specific for given metric
        """
        pass

    @property
    def value(self):
        """
        returns a value of a metric
        """
        return None
