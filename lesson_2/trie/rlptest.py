import sys
sys.path.append('src')
import rlp

test_list  = ["helloworld",
              chr(0),
              chr(126),
              "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog",
              ["Peter Piper picked a peck of pickled peppers","Betty Botter bought some butter"],
              '']  


for test in test_list:
    if isinstance(test, list):
       print("original string :" + test[0])
    else:
       print("original string :" + test)
    print("after encode : 0x" + rlp.encode(test).encode('hex'))

