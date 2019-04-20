import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode='rb')
    dest = wave.open("out.wav", mode='wb')
    
    dest.setparams(source.getparams())
    frames = source.getnframes()
    
    data = struct.unpack('<' + str(frames) + 'h', source.readframes(frames))
    
    part = len(data) // 4

    first, second = data[:part], data[part:part + part]
    third, fourth = data[part * 2:part * 3], data[part * 3:]
    
    newdata = third + fourth + first + second
    
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
            
    dest.writeframes(newframes) 
    source.close()
    dest.close()    
    