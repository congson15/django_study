def validate_query_params(request, param_names):
    valid_params = {}
    invalid_params = {}

    for param_name in param_names:
        param_value = request.GET.get(param_name)

        if param_value is not None and param_value != '':
            valid_params[param_name] = param_value
        else:
            invalid_params[param_name] = "Parameter is missing or empty."

    return valid_params, invalid_params
