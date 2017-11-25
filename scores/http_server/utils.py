class Utils:
    @staticmethod
    def get_query_param(dict, key, default_value):
        if key in dict and len(dict[key]) > 0:
            return dict[key][0]
        return default_value
