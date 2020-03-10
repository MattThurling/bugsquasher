def simple(resource_type, resources):
    print(resource_type + "s:")
    print("---------------------------------")
    for resource in resources:
        print(resource[1])
    print("---------------------------------")