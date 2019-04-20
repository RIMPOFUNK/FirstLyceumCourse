import wave
import struct


def break_the_silence():
    source = wave.open("in.wav", mode='rb')
    dest = wave.open("out.wav", mode='wb')
    
    dest.setparams(source.getparams())
    frames = source.getnframes()
    
    data = struct.unpack('<' + str(frames) + 'h', source.readframes(frames))
    
    newdata = []
    for i in data:
        if -5 <= i <= 5:
            pass
        else:
            newdata.append(i)
            
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    
    dest.writeframes(newframes) 
    source.close()
    dest.close()    
