def root_generator(values):
    for val in values:
        if val >= 0:
            result = val ** 0.5
            yield result
new_root_generator = root_generator([-5, 25, 36, -25, 0])
print(next(new_root_generator))
print(next(new_root_generator))
print(next(new_root_generator))
print(next(new_root_generator))
