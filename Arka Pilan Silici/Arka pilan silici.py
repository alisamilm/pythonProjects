from rembg import remove

input_path = "image.jpg"
output_parth =  "output.png"

with open(input_path, 'rb')as i:
    with open(output_parth, 'wb')as o:
        input_file = i.read()
        output = remove(input_file)
        o.write(output)
