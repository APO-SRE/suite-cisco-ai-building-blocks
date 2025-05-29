def dietify_schema(full_schema: dict) -> dict:
    """
    Return a *diet* version of an OpenAPI function schema:
    – keep only primitive params (string / integer / number / boolean / array)
    – drop examples, defaults, complex objects to save tokens
    """
    keep = {"string", "integer", "number", "boolean", "array"}

    full_parameters = full_schema.get("parameters", {}).get("properties", {})
    slimmed = {
        k: v
        for k, v in full_parameters.items()
        if v.get("type") in keep
    }

    diet = full_schema.copy()
    diet["parameters"]["properties"] = slimmed
    return diet
