# OpenSesame

Replacement for `open()` in python.

## Goal

Reading text files with data in C++ is surprisingly easy:

    int main() {
        ifstream myfile;
        myfile.open("data.txt");
        int records << myfile;
        double* array = new double[records];
        for (int i = 0; i < records; i++) {
            array[i] << myfile;
        }
    }

In Python, you'd have to read each line, split on words, cast to integer... yeah, forget it.
OpenSesame makes this easy:

    from open_sesame import OpenSesame

    myfile = OpenSesame("data.txt")
    records = myfile.int()
    for i in range(0, records):
        array.append(myfile.number())

## Is it fast yet?

On my 5 year old CPU, the initial working version immediately ran at reading 130 000 words per
second. I thought that should be good enough for anyone who wouldn't write a custom one anyway.

To see for yourself, run `test.py`.

If it needs to be faster, let me know what code you're using, what your data size is, and
I'll happily improve it. I like optimizing, as long as someone has a use for it :)

## Usage

Mainly, you'd use the following functions:

    from open_sesame import OpenSesame

    f = OpenSesame('/path/to/file') # no other arguments needed. Opens as read-only.

    i = f.int() # get an int

    num = f.number() # get a float/double/arbitrarily large number (this is python!)

    word = f.word() # read the next word (until a newline or whitespace character)

    ten_raw_bytes = f.bytes(10) # reads 10 bytes.

    line = f.line() # Reads until \r\n, \n or \r (in that order of preference).

    f.close() # Close the read handle

Aliases exist, so you don't have to remember which name I chose:

    f.readline() # instead of .line()

    f.string() # instead of .word()

    f.num() # instead of .number()
    f.float() # instead of .number()
    f.double() # instead of .number()

    f.integer() # instead of .int()

    f.read(length) # instead of .bytes(length)
    f.raw(length) # instead of .bytes(length)

