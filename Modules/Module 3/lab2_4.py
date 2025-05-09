


# currying example
def scale(x):
    def by(image):
        for key in image:
            image[key] *= x
        return image
    return by


def compose(f, g):
    return lambda x: f(g(x))

def rotate(x):
    def by(image):
        for key, value in image.items():
            temp = value
            image[key + 1] = value
            image[key] = temp
        return image
    return by





# 200% scale
scale_by_200 = scale(2)

# crop down to 80%
crop_to_80 = scale(.8)

#rotate twice, each time 90 deg
flip_180_deg = rotate(1)

# Test
image = {'height': 1920, 'width': 1080}


print(scale_by_200(image))
print(crop_to_80(image))
print(flip_180_deg(image))


