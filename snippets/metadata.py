from importlib.metadata import version, requires
lib_name = 'requests'
requests_version = version(lib_name)
requirements = list(requires(lib_name))

print(f'Requests version: {requests_version}')
print(f'Requirements: {requirements}')
