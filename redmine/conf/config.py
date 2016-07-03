"""
    Configuration
"""
import mydict
import config_default


configs = config_default.configs
try:
    import config_override
    configs = mydict.merge(configs, config_override.configs)
except ImportError:
    pass

configs = mydict.toDict(configs)
