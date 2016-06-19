class FeatureBroker:
    """ Feature Borker
    """
    def __init__(self, allowReplace=False):
        self.providers = {}
        self.allowReplace = allowReplace

    def provide(self, feature, provider, *args, **kwargs):
        if not self.allowReplace:
            assert not self.providers.has_key(feature), 'Duplicate feature: %r' % feature
        if callable(provider):
            def call(): return provider(*args, **kwargs)
        else:
            def call (): return provider
        self.providers[feature] = call

    def __getitem__(self, feature):
        try:
            provider = self.providers[feature]
        except KeyError:
            raise KeyError, 'Unknown feature named %r' % feature
        return provider()

features = FeatureBroker()


""" Representation of required features and feature assertions
"""

def noAssertion(obj):
    return True

def isInstanceOf(*classes):
    def test(obj): return isinstance(obj, classes)
    return test

def hasAttributes(*attributes):
    def test(obj):
        for attr in attributes:
            if not hasattr(obj, attr):
                return False
            return True
    return test

def hasMethods(*methods):
    def test(obj):
        for method in methods:
            try:
                attr = getattr(obj, method)
            except AttributeError:
                return False
            if not callable(attr):
                return False
        return True
    return test


class RequiredFeature(object):
    """ An attribute descriptor to 'declare' required features
    """
    def __init__(self, feature, assertion=noAssertion):
        self.feature = feature
        self.assertion = assertion

    def __get__(self, obj, T):
        return self.result

    def __getattr__(self, name):
        assert name == 'result', 'Unexpected attribute request other than "result"'
        self.result = self.request()
        return self.result

    def request(self):
        obj = features[self.feature]
        assert self.assertion(obj), 'The value %r of %r does not match the specified criteria'\
            % (obj, self.feature)
        return obj


