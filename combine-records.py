import glob

read_files = glob.glob("nq-train.tfrecords*")

with open("nq-train.tfrecords.combined", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
